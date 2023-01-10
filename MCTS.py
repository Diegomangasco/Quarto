import random
import quarto
import copy
import math
import RandomPlayer

class UsefulFunctions:
    '''Defines useful function for the training'''
    def __init__(self) -> None:
        pass

    def free_pieces_and_places(self, state: quarto.Quarto):
        '''Returns all possible free pieces and places for the current state'''

        board = state.get_board_status()
        free_pieces = [piece for piece in range(0, 16) if piece not in board]
        free_places = []
        for i in range(0, 3):
            for j in range(0, 3):
                if board[j, i] == -1:
                    free_places.append((i, j))

        return free_pieces, free_places

    def do_one_random_step(self, state: quarto.Quarto):
        '''Does one random game beginning on the current state to create another one'''

        free_pieces, free_places = self.free_pieces_and_places(state)
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
        self.functions = UsefulFunctions()
        self.player_id = player_id
        self.end_point = end_point

    def __hash__(self) -> int:
        return hash(bytes(self))

    def max_expansion(self) -> int:
        '''Calculates the maximum children that a node can have'''

        free_pieces, free_places = self.functions.free_pieces_and_places(self.state)
        return len(free_pieces)*len(free_places)
    
    def add_child(self, child_state: quarto.Quarto):
        '''Adds a new child to the list'''

        if child_state.check_finished() or child_state.check_winner() != -1:
            child = Node(child_state, self.player_id, self, True)
        else:
            child = Node(child_state, self.player_id, self)

        # A new random state was created and the choosing and placing part have been done randomly
        # Starting from this new state, the game will be simulated, so we need to tidy up the current player
        child.state.__current_player = (child.state.__current_player + 1) % child.state.MAX_PLAYERS 

        self.children.append(child)
        return child

    def select_child(self):
        '''Selects a child basing on the formula'''

        return max(self.children, key=lambda x: x.wins/x.visits + math.sqrt(2*math.log(self.visits)/x.visits))
    
    def update(self, result: int):
        '''Updates node statistics'''

        self.visits += 1
        self.wins += result # result can be +1 or 0

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
            elif node.children:
                if random.random() < .5: # Random decision
                    node = self.best_child(node) # Continue the search
                else:
                    if node.max_expansion() == len(node.children): # If the node reach the maximum number of children that it can have
                        node = self.best_child(node) # Continue the search
                    else:
                        return node # Expand the node
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
            if node_tmp not in [child for child in node.children]: # Control if this random expansion has already been done
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
            print("Iteration", _)
            selected_node = self.MCTS.traverse_tree(node) # SELECTION
            print("Selected node: ", selected_node)
            if selected_node == None: # Not found any expandable node
                continue
            new_node = self.MCTS.expand_tree(selected_node) # EXPANSION
            print("New node", new_node)
            if new_node.end_point: # Found an end point (leaf node)
                continue
            result = self.MCTS.simulation(new_node) # SIMULATION
            print("Print result", result)
            self.MCTS.backpropagation(new_node, result) # BACKPROPAGATION

        return self.MCTS.best_child(node)
            
