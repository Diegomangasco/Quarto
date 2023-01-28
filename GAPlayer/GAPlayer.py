import quarto
import json
from .scoreFunction import *
from RandomPlayer.RandomPlayer import RandomPlayer
from MCTS.MCTSTools import *
from HardcodedPlayer.HardcodedPlayer import HardcodedPlayer
from .quartoTrain import QuartoTrain

class GAPlayer(quarto.Player):
    '''Defines a Genetic Algorithm player'''

    def __init__(self, quarto) -> None:
        super().__init__(quarto)
        self._functions = ScoreFunction()
        self._last_state = None
        self._random_player = RandomPlayer(self.get_game())
        self._hardcoded_player = HardcodedPlayer(self.get_game())
        self._mcts_player = MCTS(0)
        with open('./GAPlayer/parameters.json', 'r') as fp:
            self._genome = json.load(fp)

    def choose_piece(self) -> int:
        board_score = self._functions.board_score(self.get_game())
        use = self.compute_diff(board_score, self._genome)
        if use == 0:
            piece = self._random_player.choose_piece()
            last_state = None
            return piece
        elif use == 1:
            piece = self._hardcoded_player.choose_piece()
            last_state = None
            return piece
        else:
            if last_state != None:
                piece = self._last_state._state.get_selected_piece()
                last_state = None
                return piece
            else:
                quarto_train = QuartoTrain(self.get_game().get_board_status(), -1, self.get_game().get_current_player())
                self._mcts_player._player_id = self.get_game().get_current_player()
                piece = self._mcts_player.do_rollout(Node(quarto_train), iterations=30)._state.get_selected_piece()
                return piece

    def place_piece(self) -> tuple[int, int]:
        board_score = self._functions.board_score(self.get_game())
        use = self.compute_diff(board_score, self._genome)
        if use == 0:
            x, y = self._random_player.place_piece()
            last_state = None
            return x, y
        elif use == 1:
            x, y = self._hardcoded_player.place_piece()
            last_state = None
            return x, y
        else:
            quarto_train = QuartoTrain(self.get_game().get_board_status(), self.get_game().get_selected_piece(), self.get_game().get_current_player())
            last_state = self._mcts_player.do_rollout(Node(quarto_train), iterations=30)
            x, y = last_state._place_where_move_current
            return x, y