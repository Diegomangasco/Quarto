import random
import quarto
import copy
import math
import RandomPlayer

class UsefulFunctions:
    '''Defines useful function for the training'''
    def __init__(self) -> None:
        pass

    def do_one_random_step(self, state: quarto.Quarto):
        '''Does one random game beginning on the current state to create another one'''

        free_pieces = [piece for piece in range(0, 16) if piece not in state.__board]
        free_places = []
        for i in range(0, 3):
            for j in range(0, 3):
                if state.__board[j, i] == -1:
                    free_places.append((i, j))
        piece = random.choice(free_pieces)
        x, y = random.choice(free_places)
        state.select(piece)
        state.place(x, y)
        return state

    def simulate_game(self, state: quarto.Quarto):
        '''Simulates a game untill the end'''

        winner = state.run()
        return winner

class Node:
    '''Defines a Node for our tree'''
    def __init__(self, state: quarto.Quarto, player_id, parent=None, end_point=False):
        self.state = state
        self.parent = parent
        self.children = list()
        self.wins = 0
        self.visits = 0
        self.player_id = player_id
        self.end_point = end_point

    def __hash__(self) -> int:
        return hash(bytes(self))
    
    def add_child(self, child_state: quarto.Quarto):
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
        self.wins += result # result can be +1 or -1

class MCTS:
    '''Defines the function to build a MCTS'''
    def __init__(self) -> None:
        self.functions = UsefulFunctions()

    def traverse_tree(self, node: Node):
        '''Traverses the tree with recursion by using the upper confidence bound for tree traversal until 
        it reaches a leaf node'''

        if not node.children and not node.end_point:
            return node # Find a node that can be expanded

        if node.end_point:
            return None # Find a leaf node, it cannot be expanded

        while node.children:
            res = self.traverse_tree(node.select_child()) # Recursion
            if res != None:
                return res

        return None

    def expand_tree(self, node: Node):
        '''Chooses randomly a possible new node'''

        # We are sure that taking a step is possible since the building of the travel function
        flag = True
        while flag:
            new_state = self.functions.do_one_random_step(copy.deepcopy(node.state))
            if new_state.check_finished() or new_state.check_winner() != -1: # Create a tmp node for checking
                node_tmp = Node(new_state, node.player_id, node, True)
            else:
                node_tmp = Node(new_state, node.player_id, node)
            if node_tmp not in [child for child in node.children]: # Control if the random expansion has already been done
                flag = False

        new_node = node.add_child(new_state) # Append a new child
        return new_node

    def simulation(self, node: Node):
        '''Simulates the game from the given state to the end'''
        
        result = self.functions.simulate_game(copy.deepcopy(node.state))
        if result == node.player_id:
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


class MCTSPlayer(quarto.Player):
    '''MonteCarlo Tree Search player'''

    def __init__(self, quarto) -> None:
        super().__init__(quarto)
        self.MCTS = MCTS()

    def choose_piece(self) -> int:
        # TODO
        return super().choose_piece()

    def place_piece(self) -> tuple[int, int]:
        # TODO
        return super().place_piece()

    def train(self, node: Node, iterations: int) -> Node:
        '''Trains the tree'''
        for _ in range(iterations):
            pending_node = self.MCTS.traverse_tree(node) # SELECTION
            if pending_node == None: # Not found any expandable node
                break
            new_node = self.MCTS.expand_tree(pending_node) # EXPANSION
            if new_node.end_point: # Found an end point
                continue
            result = self.MCTS.simulation(new_node) # SIMULATION
            self.MCTS.backpropagation(new_node, result) # BACKPROPAGATION

        return self.MCTS.best_child(node)
            
