import random as rnd
import quarto 
import numpy as np
from MCTS.API import *
from quartoTrain import *
import random
import matplotlib.pyplot as plt

class RLPlayer(quarto.Player):
    '''Defines a Reinforcement Learning player'''

    def __init__(self, quarto) -> None:
        super().__init__(quarto)
        self._quarto = quarto
        self._agent = RLTools()

    def choose_piece(self) -> int:
    # If found in _G or in MCTS, otherwise random
       pass

    def place_piece(self) -> tuple[int, int]:
       # If found in _G or in MCTS, otherwise random
       pass

class RLTools():
    '''Defines a set of Reinforcement Learning tools'''

    def __init__(self, quarto, alpha=0.15, interval=50) -> None:
        self._state_history = []  # state, reward
        self._alpha = alpha
        self._G = {}
        self._epochs = []
        self._win_percentages = []
        self._interval = interval

    def init_reward(self, hash, piece: int) -> float:
        '''Inits reward for a certain state'''

        reward = rnd.uniform(a=1.0, b=0.1)
        self._G[hash] = reward
        return reward

    def update_state_history(self, hash, reward: float) -> None:
        '''Updates the history of the visited nodes'''

        self._state_history.append((hash, reward))

    def learn(self) -> None:
        target = 0.0
        for hash, reward in reversed(self._state_history):
            self._G[hash] = self._G[hash] + self._alpha * (target - self._G[hash])
            target += reward
        self._state_history = []
        # self._random_factor -= 10e-5  # decrease random factor each episode of play

    def train(self, root: QuartoTrain, iterations=5000):
        '''Trains the RL agent against a Random Player'''

        number_win_local = 0

        for _ in range(iterations):
            lead = copy.deepcopy(root)
            our_player = 0
            lead._current_player = random.choice([0, 1])
            mcts = MCTS(our_player)

            while lead.check_winner() != -1 or lead.check_finished():

                # TODO

                if hash not in self._G.keys():
                    reward = self.init_reward(hash, piece)

                self.update_state_history(hash, reward)
                lead = new_state


            if self._api_MCTS.check_if_won(lead, our_player):
                number_win_local += 1 # If out player won
            self.learn() # Learn from experience
            # Get a history of number of steps taken to plot later
            if _ % self._interval == 0:
                print('Iteration: ', _)
                self._win_percentages.append((number_win_local/self._interval)*100)
                self._epochs.append(_)
                number_win_local = 0


        # Print graph statistics
        print('Win Rate against Random Player: ', sum(self._win_percentages)/len(self._win_percentages))
        plt.xlabel('Epochs')
        plt.ylabel('WinRate')
        plt.plot(self._epochs, self._win_percentages)
        plt.yticks(np.arange(0, max(self._win_percentages)+1, 10.0))
        plt.show()
            