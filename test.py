from MCTS.quartoTrain import *
from MCTS.MCTS import *
from RLAgent.RLAgent import *
import numpy as np
import hashlib as hash

board = QuartoTrain()
mcts = MCTS()
rlagent = RLTools()

root = Node(board, 1, -1, -1)

# print('Train MCTS with 100000 iterations')
# mcts.train(root, 100000)
print('Train RL agent with 5000 iterations')
rlagent.train(board)




