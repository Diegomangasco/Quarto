import quarto
from .MCTSTools import *

class MCTSPlayer(quarto.Player):
    '''Defines a MonteCarlo Tree Search Player'''

    def __init__(self, quarto, iterations, player_id) -> None:
        super().__init__(quarto)
        self._mcts = MCTS()
        self._iterations = iterations
        self._player_id = player_id

    def get_place(self, state, piece):
        for x in range(4):
            for y in range(4):
                if piece == state[x, y]:
                    return (x, y)

    def choose_piece(self) -> int:
        state = self.get_game().get_board_status()
        player = self.get_game().get_current_player()
        piece = self.get_game().get_selected_piece()
        place = self.get_place(state, piece) if piece != -1 else -1
        quartotrain = QuartoTrain(state, player, piece, place)
        root = Node(quartotrain, self._player_id, piece, place)
        child = self._mcts.do_rollout(root, self._iterations)
        return child._piece_to_move

    def place_piece(self) -> tuple[int, int]:
        state = self.get_game().get_board_status()
        player = self.get_game().get_current_player()
        piece = self.get_game().get_selected_piece()
        place = self.get_place(state, piece) if piece != -1 else -1
        quartotrain = QuartoTrain(state, player, piece, place)
        root = Node(quartotrain, self._player_id, piece, place)
        child = self._mcts.do_rollout(root, self._iterations)
        return child._place_where_move