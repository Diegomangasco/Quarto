import MCTS.quartoTrain as train
import MCTS.MCTS as MCTS

board = train.QuartoTrain()

root = MCTS.Node(board, 1)

mcts = MCTS.MCTS()

res = mcts.train(root, 1000)

print(root.select_child().wins/root.select_child().visits)
