import random
import copy
import math
import hashlib
import numpy as np
from .quartoTrain import * 
from .utils import *

class Node:
    '''Defines a Node for our tree. \n
    A Node is a calss that has: \n
    * A state (QuartoTrain)
    * A position where to move the current piece 
    * A number to store the wins done by passing through it
    * A number that indicates the times MCTS passes through it
    * A set of functions that are used for useful operation on the board
    * A boolean flag that indicates if the node represents an end point (final state for a board, i.e. game finished)'''

    def __init__(self, state: QuartoTrain, place_where_move_current=None, end_point=False):
        self._state = state
        self._place_where_move_current = place_where_move_current
        self._wins = 0
        self._visits = 0
        self._functions = UsefulFunctions()
        self._end_point = end_point

    def __hash__(self) -> int:
        '''Hash function for a node, it uses both the board and the piece selected by a player.'''
        t = str(self._state.get_selected_piece()) + np.array2string(self._state.get_board_status())
        val = int(hashlib.sha1(t.encode('utf-8')).hexdigest(), 32)
        return val

    def already_has_child(self, new_state: QuartoTrain):
        '''Controls if the new node that would be created is already present in node's children.'''
        
        # Since the strategy of finding symmetries has not brought very good results, I decided to not use it anymore
        board_new_state = new_state.get_board_status()
        rotate_90_clockwise, rotate_90_counter_clockwise, reflect_horizontal, reflect_vertical = self._functions.symmetries(board_new_state)
        for child in self._children:
            board_already_present = child._state.get_board_status()
            if (np.array_equal(board_new_state, board_already_present) or
                np.array_equal(rotate_90_clockwise, board_already_present) or
                np.array_equal(rotate_90_counter_clockwise, board_already_present) or
                np.array_equal(reflect_horizontal, board_already_present) or
                np.array_equal(reflect_vertical, board_already_present)):
                    return True

        return False

    def update(self, reward: int):
        '''Updates node statistics, the node was visited and brings or not to a win.'''

        self._visits += 1
        self._wins += reward # result can be +1 (win), 0.5 (draw) or 0 (loose)

    def reward(self, player_id):
        '''Establishes a reward at the end of a game. \n
        If MCTS agest won, it returns 1, if the game finished as a draw, returns 0.5 otherwise returns 0.'''

        player_who_last_moved = 1 - self._state.get_current_player()

        # 0 if plays first, 1 if plays second
        agent_position = player_id

        if player_who_last_moved == agent_position and 1 - self._state.check_winner() == agent_position:
            # MCTS won
            return 1
        elif player_who_last_moved == 1 - agent_position and 1 - self._state.check_winner() == 1 - agent_position:
            # MCTS lost
            return 0
        elif self._state.check_winner() == -1:
            # Draw game
            return 0.5

    def find_random_child(self):
        '''Makes a new Node when the game is simulated, the Node created is not added to the dictionary. \n
        The creation of the node is purely random.'''

        free_places = self._functions.free_places(self._state)
        place = random.choice(free_places)
        new_quarto = copy.deepcopy(self._state)
        new_quarto.place(place[1], place[0])
        if new_quarto.check_finished() or new_quarto.check_winner() != -1:
            # If the Node created mades the game end
            end_point = True
        else:
            free_pieces = self._functions.free_pieces(new_quarto)
            piece = random.choice(free_pieces)
            new_quarto.select(piece)
            end_point = False
        new_quarto._current_player = (new_quarto._current_player + 1) % new_quarto.MAX_PLAYERS
        return Node(new_quarto, place, end_point)

class MCTS:
    '''Defines a set of MCTS tools. \n
    The class has:
    * A set of functions that are useful to board manipulations
    * A dictionary to store all the node created during the rollout, each one with its children
    * A variable that reminds what is the ID (0 or 1) of our player'''

    def __init__(self, player_id) -> None:
        self._functions = UsefulFunctions()
        self._node_regystry = dict()
        self._player_id = player_id

    def select_child(self, node: Node):
        '''Selects a child through the node's children basing on the Upper Confidence Bound (UCB) formula. \n
        The exploration/exploitation parameter was set to sqrt(2) that is a good balance between the two approaches.'''

        points = list()
        for child in self._node_regystry[node]:
            points.append((child, child._wins/child._visits+math.sqrt(2*math.log(node._visits)/child._visits)))
    
        return max(points, key=lambda x: x[1])[0]

    def traverse_tree(self, node: Node):
        '''Traverses the tree using the Upper Confidence Bound. \n
        A list called 'path' keeps the history of all nodes visited. \n
        If a node is unexplored or terminal (cannot have children), it is immediately returned. \n
        If a node has already been explored, a child that is unexplored is chosen. \n
        If all children Have already been explored, the traversal search continues using UCB.'''

        path = []
        while True:
            path.append(node)
            if node not in self._node_regystry or not self._node_regystry[node]:
                return path # Node is unexplored or is a terminal node
            unexplored = self._node_regystry[node] - self._node_regystry.keys()
            if unexplored:
                path.append(unexplored.pop()) # Take one node unexplored
                return path
            node = self.select_child(node)

    def expand_tree(self, node: Node):
        '''Expands the node with all possible children. \n
        If a node represents an end point, its children list is set to None and the function return. \n
        Otherwise, the selected piece for the current state is placed in all possible k free positions of the board, 
        in that way we create k new configurations for the board. \n
        All pieces that have not been selected yet are taken as possible new chosen piece by the agent for the opponent. \n
        In that way we will have children that have both placed the given piece by the opponent 
        (and the position is stored in the variable of the node) and have chosen a new piece for the opponent. 
        This later is set as '__selected_piece_index' in the '_state' variable of the new node.'''

        if node._end_point:
            self._node_regystry[node] = None
            return

        free_places = self._functions.free_places(node._state)
        children = []
        for y, x in free_places:
            # Find all possible new position for the piece
            quarto = copy.deepcopy(node._state)
            quarto.place(x, y)
            if quarto.check_finished() or quarto.check_winner() != -1:
                # If the node is an end_point id doesn't make sense to choose a piece for the opponent
                children.append(Node(copy.deepcopy(quarto), (x, y),  True))
            else:
                left_pieces = self._functions.free_pieces(quarto)
                for piece in left_pieces:
                    # Select a piece for the opponent basing on the new board configuration
                    new_quarto = copy.deepcopy(quarto)
                    new_quarto.select(piece)
                    new_quarto._current_player = (new_quarto._current_player + 1) % new_quarto.MAX_PLAYERS
                    child = Node(new_quarto, (x, y))
                    children.append(child)

        self._node_regystry[node] = children # Dictionary updated
       

    def simulation(self, node: Node):
        '''Simulates the game from the given state until the end'''
        
        while True:
            if node._end_point:
                # Game finished, check the reward
                reward = node.reward(self._player_id)
                return reward
            node = node.find_random_child() # Find a random child for the current node

    def backpropagation(self, reward: int, path: list):
        '''Updates the statistics for the nodes in the 'path' list from the selected node
        to the root node, basing on the result of the simulation. \n
        The reward is inverted at each step, in that way it simulates the Min Max strategy: 
        one layer of the tree maximizes and one minimizes the reward for the agent.'''

        for node in reversed(path):
            node.update(reward)
            reward = 1 - reward # Reward inverted 

    def best_child(self, node: Node):
        '''Choose the most promising child, this operation takes count the wins and visits made on each node.'''

        if node._end_point:
            raise RuntimeError(f"choose called on terminal node {node}")

        def score(n):
            if node._visits == 0:
                return float("-inf")  # avoid unseen moves
            return node._wins / node._visits  # average reward

        return max(self._node_regystry[node], key=score)

    def function_for_training(self, node: Node, iterations: int):
        '''The basic function for the training: 
        * Select a node to expand and keep trace of its path
        * Expand the selected node
        * Simulate a game from the current node until the end of the game
        * Backpropagate the results'''

        for _ in range(iterations):
            path = self.traverse_tree(node) # SELECTION
            leaf = path[-1]
            self.expand_tree(leaf) # EXPANSION
            reward = self.simulation(leaf) # SIMULATION
            self.backpropagation(reward, path) # BACKPROPAGATION

    def do_rollout(self, root: Node, iterations: int):
        '''Trains the MCTS tree by rolling out a certain number of times.'''

        self.function_for_training(root, iterations)
        return self.best_child(root)

