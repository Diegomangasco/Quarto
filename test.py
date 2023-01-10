from MCTS import *
from quarto import *

board = quarto.Quarto()

root = Node(board, 1)

mcts = MCTSPlayer(board)

mcts.train(root, 50)