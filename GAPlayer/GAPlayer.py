import random as rnd
import quarto 
import numpy as np
from MCTS.API import *
from MCTS.quartoTrain import *
import random
from .utils import *
import matplotlib.pyplot as plt

class GAPlayer(quarto.Player):
    '''Defines a Genetic Algorithm player'''

    def __init__(self, quarto) -> None:
        super().__init__(quarto)

    def choose_piece(self) -> int:
        return super().choose_piece()

    def place_piece(self) -> tuple[int, int]:
        return super().place_piece()

class GATools():
    '''Defines a set of Genetic Algorithm tools'''

    def __init__(self, generations=100, population_size=10, offspring_size=100, games_to_play=50, random_factor=.5) -> None:
        self._generations = generations
        self._population_size = population_size
        self._offspring_size = offspring_size
        self._games_to_play = games_to_play
        self._random_factor = random_factor

    
                

    def game(self, our_player, board, genome):
        '''Simulate a certain number of games'''
        pass

    def crossover(self, gene_1, gene_2):
        '''Crossover function'''

        return  [
            {
                # XOR crossover
                'random': gene_1['random']^gene_2['random'],
                'mcts': gene_1['mcts']^gene_2['mcts'],
                'hardcoded': gene_1['hardcoded']^gene_2['hardcoded']
            },
            {
                # Random crossover
                'random': random.choice([gene_1['random'], gene_2['random']]),
                'mcts': random.choice([gene_1['mcts'], gene_2['mcts']]),
                'hardcoded': random.choice([gene_1['hardcoded'], gene_2['hardcoded']])
            }
        ]

    def mutation(self, gene_1):
        '''Mutation function'''

        while random.random() < .4:
            gene_1['random'] = random.randint(0, 15)
            gene_1['mcts'] = random.randint(0, 15)
            gene_1['hardcoded'] = random.randint(0, 15)

        return gene_1
        
    
    def evolution(self, board: QuartoTrain, our_player=0):
        '''Evolution of the genomes'''

        population = [dict() for _ in range(self._population_size)]
        for p in population:
            p['random'] = random.randint(0, 15)
            p['mcts'] = random.randint(0, 15)
            p['hardcoded'] = random.randint(0, 15)
            p['fitness'] = 0.0
        
        # Loop over generations
        for generation in range(self._generations):
            offspring = list()
            for i in range(self._offspring_size):
                # Select a gene
                selected_1, selected_2 = random.choices(population, k=2)
                if random.random() < self._random_factor:
                    # Mutation
                    new_genome = self.mutation(selected_1)
                    win = self.game(our_player, board, new_genome) # Game simulation with a certain set of parameters
                    new_fitness = win/self._games_to_play # New fitness
                    offspring.append({
                        'random': new_genome['random'],
                        'mcts': new_genome['mcts'],
                        'hardcoded': new_genome['hardcoded'],
                        'fitness': new_fitness
                    })
                else:
                    # Crossover
                    new_genome_1, new_genome_2 = self.crossover(selected_1, selected_2)
                    win_1 = self.game(our_player, board, new_genome_1) # Game simulation with a certain set of parameters
                    win_2 = self.game(our_player, board, new_genome_2)
                    new_fitness = win_1/self._games_to_play # New fitness
                    offspring.append({
                        'random': new_genome_1['random'],
                        'mcts': new_genome_1['mcts'],
                        'hardcoded': new_genome_1['hardcoded'],
                        'fitness': new_fitness
                    })
                    new_fitness = win_2/self._games_to_play # New fitness
                    offspring.append({
                        'random': new_genome_2['random'],
                        'mcts': new_genome_2['mcts'],
                        'hardcoded': new_genome_2['hardcoded'],
                        'fitness': new_fitness
                    })

            population += offspring
            population = sorted(population, key=lambda i: i['fitness'], reverse=True)[:self._population_size]
        return population[0]['random'], population[0]['mcts'], population[0]['hardcoded']