import random
import copy
import math
import json
import hashlib
import numpy as np
from .quartoTrain import * 
from .utils import *

class Node:
    '''Defines a Node for our tree'''

    def __init__(self, state: QuartoTrain, place_where_move_current=None, end_point=False):
        self._state = state
        self._place_where_move_current = place_where_move_current
        self._wins = 0
        self._visits = 0
        self._functions = UsefulFunctions()
        self._end_point = end_point

    def __hash__(self) -> int:
        t = str(self._state.get_selected_piece()) + np.array2string(self._state.get_board_status())
        val = int(hashlib.sha1(t.encode('utf-8')).hexdigest(), 32)
        return val

    def already_has_child(self, new_state: QuartoTrain):
        '''Controls if the new node that would be created is already present in node's children'''
        
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
        '''Updates node statistics'''

        self._visits += 1
        self._wins += reward # result can be +1 (win) or 0 (draw or loose)

    def reward(self, player_id):

        player_who_last_moved = 1 - self._state.get_current_player()

        # 1 if plays second, 0 if plays first
        agent_position = player_id

        if player_who_last_moved == agent_position and 1 - self._state.check_winner() == agent_position:
            # agent won
            return 1
        elif player_who_last_moved == 1 - agent_position and 1 - self._state.check_winner() == 1 - agent_position:
            # agent lost
            return 0
        elif self._state.check_winner() == -1:
            return 0.5

    def find_random_child(self):
        free_places = self._functions.free_places(self._state)
        place = random.choice(free_places)
        new_quarto = copy.deepcopy(self._state)
        new_quarto.place(place[1], place[0])
        if new_quarto.check_finished() or new_quarto.check_winner() != -1:
            end_point = True
        else:
            free_pieces = self._functions.free_pieces(new_quarto)
            piece = random.choice(free_pieces)
            new_quarto.select(piece)
            end_point = False
        new_quarto._current_player = (new_quarto._current_player + 1) % new_quarto.MAX_PLAYERS
        return Node(new_quarto, place, end_point)

class MCTS:
    '''Defines the function to build a MCTS'''

    def __init__(self, player_id) -> None:
        self._functions = UsefulFunctions()
        self._node_regystry = dict()
        self._player_id = player_id

    def select_child(self, node: Node):
        '''Selects a child basing on the specific formula'''

        points = list()
        for child in self._node_regystry[node]:
            points.append((child, child._wins/child._visits+math.sqrt(2*math.log(node._visits)/child._visits)))
    
        return max(points, key=lambda x: x[1])[0]

    def traverse_tree(self, node: Node):
        '''Traverses the tree with recursion by using the upper confidence bound for tree traversal until 
        it reaches a leaf node'''

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
        '''Expands the node with all possible children'''

        if node._end_point:
            self._node_regystry[node] = None
            return

        free_places = self._functions.free_places(node._state)
        children = []
        for y, x in free_places:
            quarto = copy.deepcopy(node._state)
            quarto.place(x, y)
            if quarto.check_finished() or quarto.check_winner() != -1:
                children.append(Node(copy.deepcopy(quarto), (x, y),  True))
            else:
                left_pieces = self._functions.free_pieces(quarto)
                for piece in left_pieces:
                    new_quarto = copy.deepcopy(quarto)
                    new_quarto.select(piece)
                    new_quarto._current_player = (new_quarto._current_player + 1) % new_quarto.MAX_PLAYERS
                    child = Node(new_quarto, (x, y))
                    children.append(child)

        self._node_regystry[node] = children
       

    def simulation(self, node: Node):
        '''Simulates the game from the given state to the end'''
        
        while True:
            if node._end_point:
                reward = node.reward(self._player_id)
                return reward
            node = node.find_random_child()

    def backpropagation(self, reward: int, path: list):
        '''Updates the statistics for the nodes on the path from the root
        to the given node, based on the result of the simulation'''

        for node in reversed(path):
            node.update(reward)
            reward = 1 - reward

    def best_child(self, node: Node):
        '''Choose the most promising child'''

        if node._end_point:
            raise RuntimeError(f"choose called on terminal node {node}")

        def score(n):
            if node._visits == 0:
                return float("-inf")  # avoid unseen moves
            return node._wins / node._visits  # average reward

        return max(self._node_regystry[node], key=score)

    def function_for_training(self, node: Node, iterations: int):
        '''The basic function for the training'''

        for _ in range(iterations):
            path = self.traverse_tree(node) # SELECTION
            leaf = path[-1]
            self.expand_tree(leaf) # EXPANSION
            reward = self.simulation(leaf) # SIMULATION
            self.backpropagation(reward, path) # BACKPROPAGATION

    def do_rollout(self, root: Node, iterations: int):
        '''Trains the tree with a MCTS'''

        self.function_for_training(root, iterations)
        return self.best_child(root)

