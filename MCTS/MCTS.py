import random
import copy
import math
import json
import numpy as np
from threading import Lock, Thread
from .quartoTrain import * 
from .lib import *

class Node:
    '''Defines a Node for our tree'''

    def __init__(self, state: QuartoTrain, player_id, piece_to_move, place_where_move, parent=None, end_point=False):
        self.state = state
        self.parent = parent
        self.children = list()
        self.piece_to_move = piece_to_move
        self.place_where_move = place_where_move
        self.wins = 0
        self.visits = 0
        self.functions = UsefulFunctions()
        self.player_id = player_id
        self.end_point = end_point
        self.lock = Lock()

    def hash_function(self):
        '''Hash function to identify a node'''

        return hash(str(self.piece_to_move) + np.array2string(self.state.get_board_status()))

    def already_has_child(self, new_state: QuartoTrain):
        '''Controls if the new node created is already present in node's children'''
        
        board_1 = new_state.get_board_status()
        for child in self.children:
            board_2 = child.state.get_board_status()
            if self.functions.equal_boards(board_1, board_2):
                return True

        return False

    def max_expansion(self) -> int:
        '''Calculates the maximum children that a node can have'''

        free_pieces, free_places = self.functions.free_pieces_and_places(self.state)
        return len(free_pieces)*len(free_places)
    
    def add_child(self, child_state: QuartoTrain, piece, place):
        '''Adds a new child to the list'''

        if child_state.check_finished() or child_state.check_winner() != -1:
            child = Node(child_state, self.player_id, piece, place, self, True)
        else:
            child = Node(child_state, self.player_id, piece, place, self) 

        self.children.append(child)
        return child

    def select_child(self):
        '''Selects a child basing on the formula'''

        return max(self.children, key=lambda x: x.wins/(x.visits if x.visits!=0 else 1) 
            + math.sqrt(2*math.log(self.visits if self.visits!=0 else 1)/(x.visits if x.visits!=0 else 1)))
    
    def update(self, result: int):
        '''Updates node statistics'''

        self.lock.acquire()
        self.visits += 1
        self.wins += result # result can be +1 (win) or 0 (draw or loose)
        self.lock.release()

class MCTS:
    '''Defines the function to build a MCTS'''

    def __init__(self) -> None:
        self.functions = UsefulFunctions()

    def traverse_tree(self, node: Node):
        '''Traverses the tree with recursion by using the upper confidence bound for tree traversal until 
        it reaches a leaf node'''

        while node.end_point == False:
            if not node.children:
                return node # Expand the node that doesn't have children
            else:
                if random.random() < .5: # Random decision
                    node = node.select_child() # Continue the traversal
                else:
                    if node.max_expansion() == len(node.children): 
                        # If the node reach the maximum number of children that it can have, continue the traversal
                        node = node.select_child()
                    else:
                        return node # Expand the node
        
        return None
        

    def expand_tree(self, node: Node):
        '''Chooses randomly a possible new node'''

        # We are sure that taking a step is possible since the building of the travel function
        node.lock.acquire()
        flag = True
        while flag:
            new_state, piece, place = self.functions.do_one_random_step(copy.deepcopy(node.state))
            if not node.already_has_child(new_state): # Control if this random expansion has already been done
                flag = False

        new_node = node.add_child(new_state, piece, place) # Append a new child
        node.lock.release()
        return new_node

    def simulation(self, node: Node):
        '''Simulates the game from the given state to the end'''
        
        result = self.functions.simulate_game(copy.deepcopy(node.state))
        if result == node.player_id: # Win
            return 1
        else:
            return 0

    def backpropagation(self, node: Node, result: int):
        '''Updates the statistics for the nodes on the path from the root
        to the given node, based on the result of the simulation'''

        while node is not None:
            node.update(result)
            node = node.parent

    def best_child(self, node: Node):
        '''Selects the child with the highest winner rate'''

        return max(node.children, key=lambda x: x.wins/x.visits)

    def function_for_training(self, node: Node, iterations: int):
        '''The basic function for the training'''

        for _ in range(iterations):
            selected_node = self.traverse_tree(node) # SELECTION
            if selected_node == None: # Not found any expandable node
                continue
            new_node = self.expand_tree(selected_node) # EXPANSION
            if new_node.end_point: # Found an end point (leaf node)
                continue
            result = self.simulation(new_node) # SIMULATION
            self.backpropagation(new_node, result) # BACKPROPAGATION

    def train(self, node: Node, iterations: int, num_threads):
        '''Trains the tree adn saves the results in a .json file'''

        thread_pool = []
        for _ in range(num_threads):
            t = Thread(target=self.function_for_training, args=(node, iterations))
            t.start()
            thread_pool.append(t)
        
        for t in thread_pool: t.join()

        tree = dict()
        self.save_tree(tree, node)

        print(len(tree.keys()))
        print(len(tree.values()))

        with open('./MCTS/database.json', 'w') as fp:
            json.dump(tree, fp)
    
    def save_tree(self, tree: dict, root: Node):
        '''Saves the nodes created in a dictionary'''

        if not root.children:
            return

        children = []
        for element in root.children:
            self.save_tree(tree, element)
            item = {
                'id': element.hash_function(), # Each element can be distinguish by its hash 
                'piece_to_move': element.piece_to_move,
                'place_where_move': element.place_where_move,
                'score': element.wins/element.visits,
                'end_node': element.end_point
            }
            children.append(item)
        tree[root.hash_function()] = children
