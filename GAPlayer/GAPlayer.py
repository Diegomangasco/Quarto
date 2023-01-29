import quarto
import json
from .scoreFunction import *
from RandomPlayer.RandomPlayer import RandomPlayer
from MCTS.MCTSTools import *
from HardcodedPlayer.HardcodedPlayer import HardcodedPlayer
from .quartoTrain import QuartoTrain

class GAPlayer(quarto.Player):
    """Genetic Algorithm Player"""

    def __init__(self, quarto) -> None:
        super().__init__(quarto)
        self._functions = ScoreFunction()
        # 'self._last_state' the child chosen with rollout operation
        # Keep track of it to know what piece to give to the opponent
        self._last_state = None 
        # Define the different players
        self._random_player = RandomPlayer(self.get_game())
        self._hardcoded_player = HardcodedPlayer(self.get_game())
        self._mcts_player = MCTS(0)
        with open('./GAPlayer/parameters.json', 'r') as fp:
            # Read parameters saved at the end of the training phase
            genome = json.load(fp)
        self._genome = dict()
        self._genome['random'] = float(genome[0])
        self._genome['hardcoded'] = float(genome[1])
        self._genome['mcts'] = float(genome[2])

    def compute_diff(self, score, genome):
        '''Computes differeces between the current board score and the genome parameters.\n
        The lowest difference indicates what is the best agent in that moment.'''

        diff = []
        diff.append(abs(score - genome['random']))
        diff.append(abs(score - genome['hardcoded']))
        diff.append(abs(score - genome['mcts']))
        return diff.index(min(diff))

    def choose_piece(self) -> int:
        board_score = self._functions.board_score(self.get_game()) # Make the scoring of the current board
        use = self.compute_diff(board_score, self._genome)
        if use == 0:
            # Use Random Player
            piece = self._random_player.choose_piece()
            self._last_state = None # Next MCTS must rollouts
            return piece
        elif use == 1:
            # Use Hardcoded Player
            piece = self._hardcoded_player.choose_piece()
            self._last_state = None # Next MCTS must rollouts
            return piece
        else:
            # Use MCTS Player
            if self._last_state != None:
                # This branch is visited only if the previous 'place_piece' was done with MCTS
                piece = self._last_state._state.get_selected_piece()
                self._last_state = None # Next MCTS must rollouts
                return piece
            else:
                # This branch is visited when the previous 'place_piece' wasn't done with MCTS
                quarto_train = QuartoTrain(self.get_game().get_board_status(), -1, self.get_game().get_current_player())
                self._mcts_player._player_id = self.get_game().get_current_player()
                piece = self._mcts_player.do_rollout(Node(quarto_train), iterations=30)._state.get_selected_piece()
                return piece

    def place_piece(self) -> tuple[int, int]:
        board_score = self._functions.board_score(self.get_game()) # Make the scoring of the current board
        use = self.compute_diff(board_score, self._genome)
        if use == 0:
            # Use Random Player
            x, y = self._random_player.place_piece()
            self._last_state = None
            return x, y
        elif use == 1:
            # Use Hardcoded Player
            x, y = self._hardcoded_player.place_piece()
            self._last_state = None
            return x, y
        else:
            # Use MCTS Player and update 'last_state' variable
            quarto_train = QuartoTrain(self.get_game().get_board_status(), self.get_game().get_selected_piece(), self.get_game().get_current_player())
            self._last_state = self._mcts_player.do_rollout(Node(quarto_train), iterations=30)
            x, y = self._last_state._place_where_move_current
            return x, y