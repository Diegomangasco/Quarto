from MCTS.quartoTrain import *
from MCTS.MCTS import *

board = QuartoTrain()

root = Node(board, 1, -1, -1)

mcts = MCTS()

mcts.train(root, 300)


