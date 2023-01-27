import random as rnd
import quarto 
import numpy as np
import random
from .ScoreFunction import ScoreFunction
from .quartoTrain import *
from RandomPlayer.RandomPlayer import RandomPlayer
from MCTS.MCTSTools import *
from HardcodedPlayer.HardcodedPlayer import HardcodedPlayer
import matplotlib.pyplot as plt

class GATools():
    '''Defines a set of Genetic Algorithm tools'''

    def __init__(self, generations=100, population_size=10, offspring_size=100, games_to_play=50, random_factor=.5, mcts_rollouts=30) -> None:
        self._generations = generations
        self._population_size = population_size
        self._offspring_size = offspring_size
        self._games_to_play = games_to_play
        self._random_factor = random_factor
        self._mcts_rollouts = mcts_rollouts
        self._functions = ScoreFunction()

    
    def control_thresholds(self, genome: dict, label):
        '''Controls thresholds for keeping the order random < hardcoded < mcts'''

        if label == 'mutation':
            v = list(genome.values())
            min_value = min(v)
            max_value = max(v)
            v.remove(min_value)
            v.remove(max_value)
            middle_value = v[0]
            return {
                'random': min_value,
                'hardcoded': middle_value,
                'mcts': max_value,
                'fitness': genome['fitness']
            }
        else:
            v = list(genome[0].values())
            min_value_1 = min(v)
            max_value_1 = max(v)
            v.remove(min_value_1)
            v.remove(max_value_1)
            middle_value_1 = v[0]
            v = list(genome[1].values())
            min_value_2 = min(v)
            max_value_2 = max(v)
            v.remove(min_value_2)
            v.remove(max_value_2)
            middle_value_2 = v[0]
            return [{
                'random': min_value_1,
                'hardcoded': middle_value_1,
                'mcts': max_value_1,
                'fitness': genome[0]['fitness']
            },
            {
                'random': min_value_2,
                'hardcoded': middle_value_2,
                'mcts': max_value_2,
                'fitness': genome[1]['fitness']
            }]

    def compute_diff(self, score, genome):
        '''Computes differeces to choose the best agent'''

        diff = []
        diff.append(abs(score - genome['random']))
        diff.append(abs(score - genome['hardcoded']))
        diff.append(abs(score - genome['mcts']))
        return diff.index(min(diff))


    def game(self, genome):
        '''Simulate a certain number of games'''
        
        win_count = 0
        for _ in range(self._games_to_play):
            q = quarto.Quarto()
            our_player = random.choice([0, 1])
            random_player = RandomPlayer(q)
            hardcoded_player = HardcodedPlayer(q)
            mcts_player = MCTS(our_player)
            last_state = None
            winner = -1
            while winner < 0 and not q.check_finished():
                piece_ok = False
                while not piece_ok:
                    if q._current_player == our_player:
                        board_score = self._functions.board_score(q)
                        use = self.compute_diff(board_score, genome)
                        if use == 0:
                            piece_ok = q.select(random_player.choose_piece())
                            last_state = None
                        elif use == 1:
                            piece_ok = q.select(hardcoded_player.choose_piece())
                            last_state = None
                        else:
                            if last_state != None:
                                piece_ok = q.select(last_state._state.get_selected_piece())
                                last_state = None
                            else:
                                quarto_train = QuartoTrain(q.get_board_status(), -1, q.get_current_player())
                                piece_ok = q.select(
                                    mcts_player.do_rollout(Node(quarto_train), iterations=self._mcts_rollouts)._state.get_selected_piece()) 
                    else:
                        piece_ok = q.select(random.randint(0, 15))
                piece_ok = False
                q._current_player = (q._current_player + 1) % q.MAX_PLAYERS
                while not piece_ok:
                    if q._current_player == our_player:
                        board_score = self._functions.board_score(q)
                        use = self.compute_diff(board_score, genome)
                        if use == 0:
                            x, y = random_player.place_piece()
                            last_state = None
                        elif use == 1:
                            x, y = hardcoded_player.place_piece()
                            last_state = None
                        else:
                            quarto_train = QuartoTrain(q.get_board_status(), q.get_selected_piece(), q.get_current_player())
                            last_state = mcts_player.do_rollout(Node(quarto_train), iterations=self._mcts_rollouts)
                            x, y = last_state._place_where_move_current
                    else:
                        x = random.randint(0, 3)
                        y = random.randint(0, 3)
                    piece_ok = q.place(x, y)
                winner = q.check_winner()

            if winner == our_player:
                win_count += 1

        return win_count

    def crossover(self, genome_1, genome_2):
        '''Crossover function'''

        return  self.control_thresholds([
            {
                # Average crossover
                'random': (genome_1['random']+genome_2['random'])*0.5,
                'hardcoded': (genome_1['hardcoded']+genome_2['hardcoded'])*0.5,
                'mcts': (genome_1['mcts']+genome_2['mcts'])*0.5,
                'fitness': genome_1['fitness'],
            },
            {
                # Random crossover
                'random': random.choice([genome_1['random'], genome_2['random']]),
                'hardcoded': random.choice([genome_1['hardcoded'], genome_2['hardcoded']]),
                'mcts': random.choice([genome_1['mcts'], genome_2['mcts']]),
                'fitness': genome_2['fitness'],
            }
        ], 'crossover')

    def mutation(self, genome_1):
        '''Mutation function'''

        while random.random() < .4:
            genome_1['random'] = random.randint(0, 16)
            genome_1['hardcoded'] = random.randint(0, 16)
            genome_1['mcts'] = random.randint(0, 16)

        return self.control_thresholds(genome_1, 'mutation')
        
    
    def evolution(self):
        '''Evolution of the genomes, trains the algorithm'''

        populat = [dict() for _ in range(self._population_size)]
        for p in populat:
            p['random'] = random.randint(0, 16)
            p['hardcoded'] = random.randint(0, 16)
            p['mcts'] = random.randint(0, 16)
            p['fitness'] = 0.0
        population = [self.control_thresholds(g, 'mutation') for g in populat]
        
        # Loop over generations
        for generation in range(self._generations):
            print('Generation number: ', generation)
            offspring = list()
            for i in range(self._offspring_size):
                # Select a gene
                selected_1, selected_2 = random.choices(population, k=2)
                if random.random() < self._random_factor:
                    # Mutation
                    new_genome = self.mutation(selected_1)
                    win = self.game(new_genome) # Game simulation with a certain set of parameters
                    new_fitness = win/self._games_to_play # New fitness
                    offspring.append({
                        'random': new_genome['random'],
                        'hardcoded': new_genome['hardcoded'],
                        'mcts': new_genome['mcts'],
                        'fitness': new_fitness
                    })
                else:
                    # Crossover
                    new_genome_1, new_genome_2 = self.crossover(selected_1, selected_2)
                    win_1 = self.game(new_genome_1) # Game simulation with a certain set of parameters
                    win_2 = self.game(new_genome_2)
                    new_fitness = win_1/self._games_to_play # New fitness
                    offspring.append({
                        'random': new_genome_1['random'],
                        'hardcoded': new_genome_1['hardcoded'],
                        'mcts': new_genome_1['mcts'],
                        'fitness': new_fitness
                    })
                    new_fitness = win_2/self._games_to_play # New fitness
                    offspring.append({
                        'random': new_genome_2['random'],
                        'hardcoded': new_genome_2['hardcoded'],
                        'mcts': new_genome_2['mcts'],
                        'fitness': new_fitness
                    })

            population += offspring
            population = sorted(population, key=lambda i: i['fitness'], reverse=True)[:self._population_size]
        return population[0]['random'], population[0]['hardcoded'], population[0]['mcts']