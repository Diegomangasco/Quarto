import json
from .quartoTrain import *
from .MCTSTools import *

# All the code refers to an old implementation for a lot of classes (like 'QuartoTrain')
# I report it only for showing that I tried also this way
class API():
    '''API to extract informations from the trained MCTS'''

    def __init__(self) -> None:
        self.mcts = MCTS()

    def create_state(self, old_state: QuartoTrain, piece: int, place: tuple):
        '''Does the action prefixed'''

        old_state.run([piece], [place])
        return copy.deepcopy(old_state)

    def check_if_won(self, state: QuartoTrain, our_player: int):
        '''Checks if the RL agent won'''

        winner = state.check_winner()
        return winner == our_player

    def load_MCTS(self) -> dict:
        '''Returns the MC tree'''

        with open('./MCTS/database.json', 'r') as fp:
            tree = json.load(fp)

        return tree

    def choose_node_using_MCTS(self, tree: dict, state: QuartoTrain, piece: int, new_piece=None, restricted=False):
        '''Chooses a node using the MCTS trained tree'''

        # Restricted is a flag that if set to True, forced to control if the piece chosen is associated with one child of the Node

        hashes = [self.mcts.functions.hash_function(piece, board) for board in self.mcts.functions.symmetries(state.get_board_status())]
        hashes.append(self.mcts.functions.hash_function(piece, state.get_board_status()))
        found = [hash for hash in hashes if hash in tree.keys() and tree[hash]['children']]
        
        if not found:
            return None
        else:
            hash = max(found, key=lambda x: tree[x]['score'])
            ids = tree[hash]['children']
            piece_place_score = [(tree[id]['piece_to_move'], tree[id]['place_where_move'], tree[id]['score']) for id in ids]
            if restricted == False:  
                return max(piece_place_score, key=lambda x: x[2])  
            else:
                restricted_moves = [p for p in piece_place_score if p[0] == new_piece]
                if restricted_moves:
                    return max(restricted_moves, key=lambda x: x[2])
                else:
                    return None
        
    def get_reward(self, node: Node):
        '''Gets the reward for a specific node'''

        return node.wins/node.visits

    def is_terminal(self, state: QuartoTrain):
        '''Checks if the state is terminal'''

        return state.check_finished() == True or state.check_winner() != -1

        

