from MCTS.quartoTrain import *
from MCTS.MCTS import *
from RLAgent.RLAgent import *
import numpy as np

board = QuartoTrain()
mcts = MCTS()
rlagent = RLPlayer(board)

root = Node(board, 1, -1, -1)

# mcts.train(root, 3000)
#print(board.get_board_status())
#print(hash(str(-1) + np.array2string(board.get_board_status())))
rlagent.train(board)




