from MCTS.quartoTrain import *
from MCTS.MCTS import *
from RLAgent.RLAgent import *

board = QuartoTrain()
mcts = MCTS()
rlagent = RLPlayer()

root = Node(board, 1, -1, -1)

# mcts.train(root, 1000)
rlagent.train(root.state)




