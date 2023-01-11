import json
import quarto
import MCTS.MCTS as mcts

class API():
    def __init__(self) -> None:
        self.mcts = mcts.MCTS()

    def search_in_db(self):
        pass

    def get_children(self, node: mcts.Node):
        return node.children

    def choose_node_using_MCTS(root: mcts.Node):
        pass

    def get_reward(self, node: mcts.Node):
        return node.wins/node.visits

    def is_terminal(self, node: mcts.Node):
        return node.end_point

    def generate_future_probs_using_MCTS(self, root: mcts.Node, node: mcts.Node):
        
        if self.search_in_db(node):
            if not self.get_children(node):
                self.mcts.train(node, 50)
            return [child.visits / root.visits for child in node.children]
        else:
            return None
        

