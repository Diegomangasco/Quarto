import quarto
import random
from MCTS.MCTSPlayer import *
from GAPlayer.GATools import *
from GAPlayer.GAPlayer import *
from HardcodedPlayer.HardcodedPlayer import *

class RandomPlayer(quarto.Player):
    """Random player"""

    def __init__(self, quarto: quarto.Quarto) -> None:
        super().__init__(quarto)

    def choose_piece(self) -> int:
        return random.randint(0, 15)

    def place_piece(self) -> tuple[int, int]:
        return random.randint(0, 3), random.randint(0, 3)

def mcts():
    wins = 0
    draws = 0
    games = 10

    for i in range(games):
        print('Game number: ', i+1)
        game = quarto.Quarto()
        game.set_players((MCTSPlayer(game), RandomPlayer(game)))
        winner = game.run()
        if winner == -1:
            draws += 1
        if winner == 0:
            wins += 1
        print('###############')

    print('Win rate: ', 100*wins/games)
    print('Draw rate: ', 100*draws/games)

def hardcoded():
    wins = 0
    draws = 0
    games = 1000

    for i in range(games):
        print('Game number: ', i+1)
        game = quarto.Quarto()
        hardcoded_player = random.randint(0, 1)
        if hardcoded_player == 0:
            game.set_players((HardcodedPlayer(game), RandomPlayer(game)))
        else:
            game.set_players((RandomPlayer(game), HardcodedPlayer(game)))
        winner = game.run()
        if winner == -1:
            draws += 1
        if winner == hardcoded_player:
            wins += 1
        print('###############')

    print('Win rate: ', 100*wins/games, '%')
    print('Draw rate: ', 100*draws/games, '%')

def gatools():
    gatools = GATools(generations=100, population_size=10, offspring_size=50, games_to_play=6)
    print(gatools.evolution())

def ga():
    wins = 0
    draws = 0
    games = 10

    for i in range(games):
        print('Game number: ', i+1)
        game = quarto.Quarto()
        game.set_players((GAPlayer(game), RandomPlayer(game)))
        winner = game.run()
        if winner == -1:
            draws += 1
        if winner == 0:
            wins += 1
        print('###############')

    print('Win rate: ', 100*wins/games)
    print('Draw rate: ', 100*draws/games)

# mcts()
#hardcoded()
gatools()
# ga()


