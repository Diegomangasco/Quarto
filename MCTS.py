import random
import quarto
import copy
import math
import RandomPlayer

class Node:
    def __init__(self, state: quarto.Quarto, player_id, parent=None):
        self.state = state
        self.parent = parent
        self.children = list()
        self.wins = 0
        self.visits = 0
        self.player_id = player_id
    
    def add_child(self, child_state: quarto.Quarto):
        child = Node(child_state, self.player_id, self)
        self.children.append(child)
        return child

    def select_child(self):
        return max(self.children, key=lambda x: x.wins/x.visits + math.sqrt(2*math.log(self.visits)/x.visits))
    
    def update(self, result: quarto.Quarto):
        self.visits += 1
        if result.check_winner() == self.player_id: # Our player 
            self.wins += 1
        else:
            self.wins -= 1

class MCTSPlayer(quarto.Player):
    '''MonteCarlo Tree Search player'''

    def __init__(self, quarto) -> None:
        super().__init__(quarto)
        self.MAX_PLAYERS = 2

    def choose_randomly(self):
        return random.randint(0, 15)

    def place_randomly(self):
        return random.randint(0, 3), random.randint(0, 3)

    def choose_piece(self) -> int:
        # TODO
        return super().choose_piece()

    def place_piece(self) -> tuple[int, int]:
        # TODO
        return super().place_piece()

    def search(self, node: Node, iterations: int) -> Node:
        for _ in range(iterations):

            # SELECTION
            selected_node = node
            if selected_node.children:
                while selected_node.children:

                    selected_node = selected_node.select_child()

                    if selected_node.state.check_finished() or selected_node.state.check_winner() != -1:
                        selected_node.update(selected_node.state) # The game is terminated
                    else:
                        # EXPANSION

                        # Choose randomly a possible moves -> new_node
                        # TODO a function to have all possible states and pick randomly one

                        selected_node = selected_node.add_child(new_node) # Found a new node (new state)

                        # SIMULATION
                        game = copy.deepcopy(selected_node.state)
                        our_player = RandomPlayer.RandomPlayer(game)
                        other_player = RandomPlayer.RandomPlayer(game)
                        if node.player_id == 0:
                            game.set_players(our_player, other_player)
                        else:
                            game.set_players(other_player, our_player)
                        game.run()

                        # BACKPROPAGATION
                        while selected_node is not None:
                            selected_node.update(game)
                            selected_node = selected_node.parent
            else:
                # EXPANSION
                # TODO
                pass

        return max(node.children, key=lambda x: x.wins/x.visits)
            

