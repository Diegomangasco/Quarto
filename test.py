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
draws = 0
games = 10
mcts = None

for i in range(games):
    print('Game number: ', i+1)
    game = quarto.Quarto()
    player = MCTSPlayer(game, 0, iterations=30)
    game.set_players((player, RandomPlayer(game)))
    winner = game.run()
    if winner == -1:
        draws += 1
    if winner == 0:
        wins += 1
    print('###############')

print('Win rate: ', 100*wins/games)
print('Draw rate: ', 100*draws/games)


