import quarto
import copy
import math
import RandomPlayer

class Node:
    def __init__(self, state: quarto.Quarto, parent=None):
        self.state = state
        self.parent = parent
        self.children = list()
        self.wins = 0
        self.visits = 0
    
    def add_child(self, child_state: quarto.Quarto):
        child = Node(child_state, self)
        self.children.append(child)
        return child

    def select_child(self):
        return max(self.children, key=lambda x: x.wins/x.visits + math.sqrt(2*math.log(self.visits)/x.visits))
    
    def update(self, result: quarto.Quarto):
        self.visits += 1
        if result.check_winner() == 1:
            self.wins += 1

class MCTSPlayer(quarto.Player):
    '''MonteCarlo Tree Search player'''

    def __init__(self, quarto) -> None:
        super().__init__(quarto)

    def choose_piece(self) -> int:
        return super().choose_piece()

    def place_piece(self) -> tuple[int, int]:
        return super().place_piece()

    def search(node: Node, iterations: int) -> Node:
        for _ in range(iterations):

            # Selection phase
            selected_node = node
            while selected_node.children:

                selected_node = selected_node.select_child()

                # Expansion phase
                if selected_node.state.check_finished() or selected_node.state.check_winner() != -1:
                    selected_node.update(selected_node.state)
                else:
                    rp = RandomPlayer.RandomPlayer(selected_node.state)
                    sn = copy.deepcopy(selected_node)
                    piece_ok = False
                    while not piece_ok:
                        piece_ok = sn.state.select(rp.choose_piece())
                    piece_ok = False
                    while not piece_ok:
                        x, y = rp.place_piece()
                        piece_ok = sn.state.place(x, y)
                        
                    selected_node = selected_node.add_child(sn.state)

                    # Simulation

                    # Backpropagation
                    while selected_node is not None:
                        selected_node.update(selected_node.state)
                        selected_node = selected_node.parent

        return max(node.children, key=lambda x: x.wins/x.visits)
            

