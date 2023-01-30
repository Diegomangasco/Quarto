import quarto
from .MCTSTools import *

class MCTSPlayer(quarto.Player):
    """MonteCarlo Tree Search (MCTS) Player"""

    def __init__(self, quarto, iterations=30) -> None:
        super().__init__(quarto)
        self._mcts = MCTS(0)
        self._iterations = iterations # Iterations for rollout
        # It's the child chosen with rollout operation
        # Keep track of it to know what piece to give to the opponent
        self._last_state = None 

    def choose_piece(self) -> int:
        if self._last_state == None:
            # The only case this branch is taken is when MCTS agent plays the first turn as player 0
            return random.randint(0, 15)
        else:
            # Take the piece by the stored information
            return self._last_state._state.get_selected_piece()

    def place_piece(self) -> tuple[int, int]:
        board = self.get_game().get_board_status()
        piece = self.get_game().get_selected_piece()
        player = self.get_game().get_current_player()
        quartotrain = QuartoTrain(board, piece, player)
        root = Node(quartotrain)
        self._mcts._player_id = self.get_game().get_current_player()
        child = self._mcts.do_rollout(root, self._iterations) # Launch rollout for MCTS
        self._last_state = child # Save the child 
        return child._place_where_move_current