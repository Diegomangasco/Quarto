import random
import copy
import math
import json
import hashlib as hash
import numpy as np
from .quartoTrain import * 
from .utils import *

class Node:
    '''Defines a Node for our tree'''

    def __init__(self, state: QuartoTrain, piece_to_move, end_point=False):
        self._state = state
        self._piece_to_move = piece_to_move
        self._wins = 0
        self._visits = 0
        self._functions = UsefulFunctions()
        self._end_point = end_point

    def __hash__(self) -> int:
        string = str(self._piece_to_move) + np.array2string(self._state.get_board_status())
        string = string.encode('utf-8')
        return hash.sha1(string).hexdigest()

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
    
    def add_child(self, child_state: QuartoTrain, piece, place):
        '''Adds a new child to the list'''

        if child_state.check_finished() or child_state.check_winner() != -1:
            child = Node(child_state, self._player_id, piece, place, self, True)
        else:
            child = Node(child_state, self._player_id, piece, place, self) 

        self._children.append(child)
        return child

    def select_child(self):
        '''Selects a child basing on the specific formula'''

        points = list()
        for child in self._children:
            points.append((child, child._wins/child._visits+math.sqrt(2*math.log(self._visits)/child._visits)))
    
        return max(points, key=lambda x: x[1])[0]

    def update(self, result: int):
        '''Updates node statistics'''

        self._visits += 1
        self._wins += result # result can be +1 (win) or 0 (draw or loose)

class MCTS:
    '''Defines the function to build a MCTS'''

    def __init__(self, player_id) -> None:
        self._functions = UsefulFunctions()
        self._node_regystry = dict()
        self._player_id = player_id

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
            node = node.select_child()

    def expand_tree(self, node: Node):
        '''Expands the node with all possible children'''

        if node._end_point:
            return

        free_places = self._functions.free_places(node._state)
        children = []
        for x, y in free_places:
            board = node._state.get_board_status()
            board[x, y] = node._piece_to_move
            quarto = QuartoTrain(board, node._state._current_player, node._piece_to_move, (x, y))
            if quarto.check_finished() or quarto.check_winner() != -1:
                children.append(Node(quarto, piece, True))
            else:
                left_pieces = self._functions.free_pieces(quarto)
                for piece in left_pieces:
                    child = Node(quarto, piece)
                    children.append(child)

        self._node_regystry[node] = children
       

    def simulation(self, node: Node):
        '''Simulates the game from the given state to the end'''
        
        child = random.choice(self._node_regystry[node])
        return self._functions.simulate_game(copy.deepcopy(child._state))

    def backpropagation(self, reward: int, path: list):
        '''Updates the statistics for the nodes on the path from the root
        to the given node, based on the result of the simulation'''

        for node in reversed(path):
            node.update(reward)
            result = 1 - reward

    def best_child(self, node: Node):
        '''Choose the most promising child'''

        if node._end_point:
            raise RuntimeError(f"choose called on terminal node {node}")

        if node not in self._node_regystry:
            free_places = self._functions.free_places(node._state)
            place = random.choice(free_places)
            free_places.remove(place)
            board = node._state.get_board_status()
            board[place[0], place[1]] = node._piece_to_move
            quarto = QuartoTrain(board, node._state._current_player, node._piece_to_move, (place[0], place[1]))
            piece = random.choice(self._functions.free_pieces(quarto))
            return Node(quarto, piece)

        def score(n):
            if node._visits == 0:
                return float("-inf")  # avoid unseen moves
            return node._wins / node._visits  # average reward

        return max(self._node_regystry[node], key=score)

    def function_for_training(self, node: Node, iterations: int):
        '''The basic function for the training'''

        for _ in range(iterations):
            path = self.traverse_tree(node) # SELECTION
            self.expand_tree(path[-1]) # EXPANSION
            reward = self.simulation(path[-1]) # SIMULATION
            self.backpropagation(reward, path) # BACKPROPAGATION

    def do_rollout(self, root: Node, iterations: int):
        '''Trains the tree with a MCTS'''

        self.function_for_training(root, iterations)
        return self.best_child(root)

    def wrapper_save_tree(self, root: Node):
        tree = dict()
        item_root = self.save_tree(tree, root)
        tree[root.__hash__()] = item_root

        with open('./MCTS/database.json', 'w') as fp:
            json.dump(tree, fp)
    
    def save_tree(self, tree: dict, node: Node):
        '''Saves the nodes created in a dictionary'''

        if not node.children:
            return {
                'piece_to_move': node.piece_to_move,
                'place_where_move': node.place_where_move,
                'score': node.wins/node.visits,
                'end_node': node.end_point,
                'children': []
            }

        children = []
        for element in node.children:
            child = self.save_tree(tree, element)
            hash = element.__hash__()
            tree[hash] = child
            children.append(hash)

        item = {
            'piece_to_move': node.piece_to_move,
            'place_where_move': node.place_where_move,
            'score': node.wins/node.visits,
            'end_node': node.end_point,
            'children': children
        }

        return item
