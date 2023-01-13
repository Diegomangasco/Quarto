from MCTS.quartoTrain import *
from MCTS.MCTS import *

board = QuartoTrain()

root = Node(board, 1, -1, -1)

mcts = MCTS()

res = mcts.train(root, 10)

print(root.select_child().wins/root.select_child().visits)
