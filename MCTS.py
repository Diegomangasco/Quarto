import random
import copy
import math
import quartoTrain as train
import lib

class Node:
    '''Defines a Node for our tree'''

    def __init__(self, state: train.QuartoTrain, player_id, parent=None, end_point=False):
        self.state = state
        self.parent = parent
        self.children = list()
        self.wins = 0
        self.visits = 0
        self.functions = lib.UsefulFunctions()
        self.player_id = player_id
        self.end_point = end_point

    def __hash__(self) -> int:
        return hash(bytes(self))

    def already_has_child(self, new_state: train.QuartoTrain):
        '''Controls if the state created is already present in node's children'''
        
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
    
    def add_child(self, child_state: train.QuartoTrain):
        '''Adds a new child to the list'''

        if child_state.check_finished() or child_state.check_winner() != -1:
            child = Node(child_state, self.player_id, self, True)
        else:
            child = Node(child_state, self.player_id, self) 

        self.children.append(child)
        return child

    def select_child(self):
        '''Selects a child basing on the formula'''

        return max(self.children, key=lambda x: x.wins/x.visits + math.sqrt(2*math.log(self.visits)/x.visits))
    
    def update(self, result: int):
        '''Updates node statistics'''

        self.visits += 1
        self.wins += result # result can be +1 (win) or 0 (draw or loose)

class MCTS:
    '''Defines the function to build a MCTS'''
    def __init__(self) -> None:
        self.functions = lib.UsefulFunctions()

    def traverse_tree(self, node: Node):
        '''Traverses the tree with recursion by using the upper confidence bound for tree traversal until 
        it reaches a leaf node'''

        while node.end_point == False:
            if not node.children:
                return node # Expand the node that doesn't have children
            else:
                if random.random() < .5: # Random decision
                    node = self.best_child(node) # Continue the traversal
                else:
                    if node.max_expansion() == len(node.children): 
                        # If the node reach the maximum number of children that it can have, continue the traversal
                        node = self.best_child(node)
                    else:
                        return node # Expand the node
        
        return None
        

    def expand_tree(self, node: Node):
        '''Chooses randomly a possible new node'''

        # We are sure that taking a step is possible since the building of the travel function
        flag = True
        while flag:
            new_state = self.functions.do_one_random_step(copy.deepcopy(node.state))
            if not node.already_has_child(new_state): # Control if this random expansion has already been done
                flag = False

        new_node = node.add_child(new_state) # Append a new child
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


class MCTSTrain():
    '''MonteCarlo Tree Search class for training the tree'''

    def __init__(self) -> None:
        self.MCTS = MCTS()

    def train(self, node: Node, iterations: int) -> Node:
        '''Trains the tree'''

        for _ in range(iterations):
            selected_node = self.MCTS.traverse_tree(node) # SELECTION
            if selected_node == None: # Not found any expandable node
                continue
            new_node = self.MCTS.expand_tree(selected_node) # EXPANSION
            if new_node.end_point: # Found an end point (leaf node)
                continue
            result = self.MCTS.simulation(new_node) # SIMULATION
            self.MCTS.backpropagation(new_node, result) # BACKPROPAGATION

        return self.MCTS.best_child(node)
            
