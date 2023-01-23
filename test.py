import quarto
import random
from MCTS.MCTSPlayer import *

class RandomPlayer(quarto.Player):
    """Random player"""

    def __init__(self, quarto: quarto.Quarto) -> None:
        super().__init__(quarto)

    def choose_piece(self) -> int:
        return random.randint(0, 15)

    def place_piece(self) -> tuple[int, int]:
        return random.randint(0, 3), random.randint(0, 3)


wins = 0
games = 50

for i in range(games):
    print('Game number: ', i+1)
    game = quarto.Quarto()
    if i%2 != 0:
        our_player = MCTSPlayer(game, 0, iterations=90)
        game.set_players((our_player, RandomPlayer(game)))
    else:
        our_player = MCTSPlayer(game, 1, iterations=90)
        game.set_players((RandomPlayer(game), our_player))
    winner = game.run()
    if winner == 1:
        wins += 1
    print('###############')

print('Win rate: ', 100*wins/games)


