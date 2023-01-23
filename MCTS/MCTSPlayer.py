import quarto
from .MCTSTools import *

class MCTSPlayer(quarto.Player):
    '''Defines a MonteCarlo Tree Search Player'''

    def __init__(self, quarto, player_id, iterations=50, mcts=None) -> None:
        super().__init__(quarto)
        self._mcts = MCTS(player_id)
        self._player_id = player_id
        self._iterations = iterations
        self._last_state = None

    def choose_piece(self) -> int:
        if self._last_state == None:
            return random.randint(0, 15)
        else:
            print(self._last_state._piece_to_move_next)
            return self._last_state._piece_to_move_next

    def place_piece(self) -> tuple[int, int]:
        state = self.get_game().get_board_status()
        piece = self.get_game().get_selected_piece()
        quartotrain = QuartoTrain(state, self._player_id)
        root = Node(quartotrain, piece)
        child = self._mcts.do_rollout(root, self._iterations)
        self._last_state = child
        return child._place_where_move_current