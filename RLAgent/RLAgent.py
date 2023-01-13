import random as rnd
import quarto 
import numpy as np
from ..MCTS.API import *
import random
import matplotlib as plt

class RLPlayer(quarto.Player):
    '''Defines a Reinforcement Learning player'''

    def __init__(self, quarto, alpha=0.15, gamma=0.15, random_factor = 0.2) -> None:
        super().__init__(quarto)
        self._state_history = []  # state, reward
        self._alpha = alpha
        self._gamma = gamma
        self._random_factor = random_factor
        self._G = {}
        self._api_MCTS = API()
        self._epochs = []
        self._wins = []

    def choose_piece(self) -> int:
        maxG = -10e15
        next_move = None
        randomN = rnd.random()
        if randomN < self._random_factor:
            # if random number below random factor, choose random action
            new_state, next_move = rnd.choice(allowedStates)
            if new_state not in self._G.keys():
                self.init_reward(new_state)
        else:
            # if exploiting, gather all possible actions and choose one with the highest G (reward)
            for state in allowedStates:
                new_state = state[0]
                if new_state not in self._G.keys():
                    self.init_reward(new_state)
                if self._G[new_state] >= maxG:
                    next_move = state[1]
                    maxG = self._G[new_state]
        return next_move

    def place_piece(self) -> tuple[int, int]:
        maxG = -10e15
        next_move = None
        randomN = rnd.random()
        if randomN < self._random_factor:
            # if random number below random factor, choose random action
            new_state, next_move = rnd.choice(allowedStates)
            if new_state not in self._G.keys():
                self.init_reward(new_state)
        else:
            # if exploiting, gather all possible actions and choose one with the highest G (reward)
            for state in allowedStates:
                new_state = state[0]
                if new_state not in self._G.keys():
                    self.init_reward(new_state)
                if self._G[new_state] >= maxG:
                    next_move = state[1]
                    maxG = self._G[new_state]
        return next_move

    def get_related_nodes(self, node):
        return self._api_MCTS.get_children(node)

    def init_reward(self, state: quarto.Quarto) -> float:
        '''Inits reward for a certain state'''

        reward = rnd.uniform(a=1.0, b=0.1)
        self._G[state] = reward
        return reward

    def update_state_history(self, state: quarto.Quarto, reward: float) -> None:
        '''Updates the history of the visited nodes'''
        if (state, reward) not in self._state_history:
            self._state_history.append((state, reward))

    def learn(self) -> None:
        target = 0
        for prev, reward in reversed(self._state_history):
            future_probabilities = self._api_MCTS.generate_future_probs_using_MCTS(prev)
            if future_probabilities:
                expected_values = np.dot(future_probabilities, self.get_related_nodes(prev))
                self._G[tuple(prev)] = (1-self._alpha)*self._G[tuple(prev)] + self._alpha*(target*self._gamma*np.max(expected_values) - self._G[tuple(prev)])
            else:
                self._G[tuple(prev)] = (1-self._alpha)*self._G[tuple(prev)] + self._alpha*(target - self._G[tuple(prev)])
            target += reward
        self._state_history = []
        self._random_factor -= 10e-5  # decrease random factor each episode of play

    def train(self, root, iterations=5000):
        '''Trains the RL agent against a Random Player'''

        number_win_local = 0
        for _ in range(iterations):
            lead = root.state
            our_player = 0
            current_player = random.choice([0, 1])

            while not self._api_MCTS.is_terminal(lead):

                if our_player == current_player:
                    piece_place_score = self._api_MCTS.choose_node_using_MCTS(lead)

                    if not piece_place_score:
                        # Node not present in database, do a random action
                        new_state=#TODO
                    
                        if new_state not in self._G.keys():
                            reward = self.init_reward(new_state)
                        else:
                            reward = self._G[new_state]
                    else:
                        new_state = self._api_MCTS.create_state(lead, piece_place_score)
                        reward = piece_place_score[2]
                        if new_state not in self._G.keys():
                            self._G[new_state] = reward

                    self.update_state_history(new_state, reward)
                    lead = new_state
                    current_player = 1

                else:
                    # Random player
                    new_state = #TODO
                    lead = new_state
                    current_player = 0

            if self._api_MCTS.check_if_won(lead, our_player):
                # If out player won
                number_win_local += 1

            self.learn() # Learn from experience

            # Get a history of number of steps taken to plot later
            if _ % 50 == 0:
                self._wins.append(number_win_local)
                self._epochs.append(_)
                number_win_local = 0

        # Print graph statistics
        plt.semilogy(self._epochs, self._wins, "b")
        plt.show()
            