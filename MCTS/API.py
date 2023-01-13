import json
import quarto
from .MCTS import *

class API():
    '''API to extract informations from the trained MCTS'''

    def __init__(self) -> None:
        self.mcts = MCTS()

    def search_in_db(self):
        pass

    def get_children(self, node: Node):
        return node.children

    def check_if_won(self, state: quarto.Quarto, our_player: int):
        '''Checks if the RL agent won'''

        winner = state.check_winner()
        return winner == our_player

    def choose_node_using_MCTS(root: quarto.Quarto):
        '''Chooses a node using the MCTS trained'''

        root_id = root.id
        children = list()
        with open('./MCTS/database.json', 'r') as fp:
            json_array = json.load(fp)
        
        for item in json_array:
            if item['parent_id'] == root_id:
                # Search for all the nodes that have as a parent the current one
                children.append((item['piece_to_move'], item['place_where_move'], item['score']))

        if children:
            return max(children, key=lambda x: x[2])

        return None

    def get_reward(self, node: Node):
        '''Gets the reward for a specific node'''

        return node.wins/node.visits

    def is_terminal(self, state: quarto.Quarto):
        '''Checks if the state is terminal'''

        return state.check_finished() == True or state.check_winner() != -1

    def generate_future_probs_using_MCTS(self, root: Node, node: Node):
        
        if self.search_in_db(node):
            if not self.get_children(node):
                pass
            return [child.visits / root.visits for child in node.children]
        else:
            return None
        

