import quarto
from .MCTSTools import *

class MCTSPlayer(quarto.Player):
    '''Defines a MonteCarlo Tree Search Player'''

    def __init__(self, quarto, player_id, iterations=50) -> None:
        super().__init__(quarto)
        self._mcts = MCTS(player_id)
        self._player_id = player_id
        self._iterations = iterations
        self._last_state = None

    def get_mcts(self):
        return self._mcts

    def choose_piece(self) -> int:
        if self._last_state == None:
            return random.randint(0, 15)
        else:
            return self._last_state._state.get_selected_piece()

    def place_piece(self) -> tuple[int, int]:
        state = self.get_game().get_board_status()
        piece = self.get_game().get_selected_piece()
        player = self.get_game().get_current_player()
        quartotrain = QuartoTrain(state, piece, player)
        root = Node(quartotrain)
        child = self._mcts.do_rollout(root, self._iterations)
        self._last_state = child
        return child._place_where_move_current