import random as rnd
import quarto 
import numpy as np
from ..MCTS.API import *
from ..MCTS.quartoTrain import *
import random
import matplotlib as plt

class RLPlayer(quarto.Player):
    '''Defines a Reinforcement Learning player'''

    def __init__(self, quarto, alpha=0.15) -> None:
        super().__init__(quarto)
        self._state_history = []  # state, reward
        self._alpha = alpha
        # self._random_factor = random_factor
        self._G = {}
        self._api_MCTS = API()
        self._epochs = []
        self._wins = []

    def choose_piece(self) -> int:
    # If found in _G, otherwise random
       pass

    def place_piece(self) -> tuple[int, int]:
       # If found in _G, otherwise random
       pass

    def init_reward(self, hash, piece: int) -> float:
        '''Inits reward for a certain state'''

        reward = rnd.uniform(a=1.0, b=0.1)
        self._G[hash] = reward
        return reward

    def update_state_history(self, hash, reward: float) -> None:
        '''Updates the history of the visited nodes'''

        self._state_history.append((hash, reward))

    def learn(self) -> None:
        target = 0
        for hash, reward in reversed(self._state_history):
            self._G[tuple(hash)] = self._G[tuple(hash)] + self._alpha * (target - self._G[tuple(hash)])
            target += reward
        self._state_history = []
        # self._random_factor -= 10e-5  # decrease random factor each episode of play

    def train(self, root: QuartoTrain, iterations=5000):
        '''Trains the RL agent against a Random Player'''

        number_win_local = 0
        tree = self._api_MCTS.load_MCTS()
        for _ in range(iterations):
            lead = copy.deepcopy(root)
            our_player = 0
            lead._current_player = random.choice([0, 1])

            piece = -1

            while not self._api_MCTS.is_terminal(lead):

                if our_player == lead._current_player: # Agent chooses, Random places

                    piece_place_score = self._api_MCTS.choose_node_using_MCTS(tree, lead, piece)

                    if not piece_place_score:
                        # Not present in our MCTS database
                        free_pieces, free_places = self._api_MCTS.mcts.functions.free_pieces_and_places(lead)
                        piece = random.choice(free_pieces)
                        flag_random = True
                    
                    else:
                        piece = piece_place_score[0]
                        flag_random = False
                    
                    place = random.choice(free_places) # Random player

                else: # Random chooses, Agent places
                    free_pieces, free_places = self._api_MCTS.mcts.functions.free_pieces_and_places(lead)
                    _piece = random.choice(free_pieces) # Random player
                    
                    place_score = self._api_MCTS.choose_node_using_MCTS(tree, lead, piece, _piece, restricted=True)

                    if not place_score:
                        # Not present in our MCTS database
                        place = random.choice(free_places)
                        flag_random = True
                    else:
                        place = place_score[1]
                        flag_random = False

                    piece = _piece

                new_state = self._api_MCTS.create_state(lead, piece, place)
                hash = self._api_MCTS.mcts.functions.hash_function(piece, new_state.get_board_status())

                if hash not in self._G.keys():
                    if flag_random:
                        reward = self.init_reward(hash, piece)
                    else:
                        reward = piece_place_score[2]
                        self._G[hash] = reward

                self.update_state_history(hash, reward)
                lead = new_state


            if self._api_MCTS.check_if_won(lead, our_player):
                number_win_local += 1 # If out player won
            self.learn() # Learn from experience
            # Get a history of number of steps taken to plot later
            if _ % 50 == 0:
                self._wins.append(number_win_local)
                self._epochs.append(_)
                number_win_local = 0


        # Print graph statistics
        plt.semilogy(self._epochs, self._wins, "b")
        plt.show()
            