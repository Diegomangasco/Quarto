import quarto 
import random
import json
from .scoreFunction import ScoreFunction
from .quartoTrain import *
from RandomPlayer.RandomPlayer import RandomPlayer
from MCTSPlayer.MCTSTools import *
from HardcodedPlayer.HardcodedPlayer import HardcodedPlayer

# This variable was set after some trials (heuristics)
GENOME_VAL_UPPER_BOUND = 10 

class GATools():
    '''Defines a set of Genetic Algorithm tools. \n
    The class has:
    * A variable for the number of generations
    * A variable for the population size
    * A variable for the offspring size
    * A variable that tells how many games play for each offspring element
    * A variable for the random factor (decide between mutation or crossover)
    * A variable that tells how many rollouts do with MCTS
    * A function for scoring the board'''

    def __init__(self, generations=100, population_size=10, offspring_size=100, games_to_play=50, random_factor=.5, mcts_rollouts=30) -> None:
        self._generations = generations
        self._population_size = population_size
        self._offspring_size = offspring_size
        self._games_to_play = games_to_play # How many games play for each offspring element
        self._random_factor = random_factor
        self._mcts_rollouts = mcts_rollouts # How many rollouts do with MCTS
        self._functions = ScoreFunction()        

    def compute_diff(self, score, genome):
        '''Computes differeces between the current board score and the genome parameters.\n
        The lowest difference indicates what is the best agent in that moment.'''

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
            # Define players
            random_player = RandomPlayer(q)
            hardcoded_player = HardcodedPlayer(q)
            mcts_player = MCTS(our_player)
            # 'last_state' the child chosen with rollout operation
            # Keep track of it to know what piece to give to the opponent
            last_state = None
            winner = -1
            # Game starts
            while winner < 0 and not q.check_finished():
                piece_ok = False
                while not piece_ok:
                    if q._current_player == our_player:
                        board_score = self._functions.board_score(q)
                        use = self.compute_diff(board_score, genome)
                        if use == 0:
                            # Use Random Player
                            piece_ok = q.select(random_player.choose_piece())
                            last_state = None # Next MCTS must rollouts
                        elif use == 1:
                            # Use Hardcoded Player
                            piece_ok = q.select(hardcoded_player.choose_piece())
                            last_state = None # Next MCTS must rollouts
                        else:
                            # Use MCTS player
                            if last_state != None:
                                # This branch is visited only if the previous 'place_piece' was done with MCTS
                                piece_ok = q.select(last_state._state.get_selected_piece())
                                last_state = None # Next MCTS must rollouts
                            else:
                                # This branch is visited when the previous 'place_piece' wasn't done with MCTS
                                quarto_train = QuartoTrain(q.get_board_status(), -1, q.get_current_player())
                                piece_ok = q.select(
                                    mcts_player.do_rollout(Node(quarto_train), iterations=self._mcts_rollouts)._state.get_selected_piece()) 
                    else:
                        # Opponent (Random Player)
                        piece_ok = q.select(random.randint(0, 15))
                piece_ok = False
                q._current_player = (q._current_player + 1) % q.MAX_PLAYERS
                while not piece_ok:
                    if q._current_player == our_player:
                        board_score = self._functions.board_score(q)
                        use = self.compute_diff(board_score, genome)
                        if use == 0:
                            # Use Random Player
                            x, y = random_player.place_piece()
                            last_state = None # Next MCTS must rollouts
                        elif use == 1:
                            # Use Hardcoded Player
                            x, y = hardcoded_player.place_piece()
                            last_state = None # Next MCTS must rollouts
                        else:
                            # Use MCTS Player and update 'last_state'
                            quarto_train = QuartoTrain(q.get_board_status(), q.get_selected_piece(), q.get_current_player())
                            last_state = mcts_player.do_rollout(Node(quarto_train), iterations=self._mcts_rollouts)
                            x, y = last_state._place_where_move_current
                    else:
                        # Opponent (Random Player)
                        x = random.randint(0, 3)
                        y = random.randint(0, 3)
                    piece_ok = q.place(x, y)
                winner = q.check_winner()

            if winner == our_player:
                win_count += 1

        return win_count

    def control_thresholds(self, genome: dict):
        '''Controls thresholds for keeping the order random < hardcoded < mcts'''

        if genome['random'] > genome['hardcoded']:
            genome['random'], genome['hardcoded'] = genome['hardcoded'], genome['random']
        if genome['hardcoded'] > genome['mcts']:
            genome['hardcoded'], genome['mcts'] = genome['mcts'], genome['hardcoded']
        if genome['random'] > genome['hardcoded']:
            genome['random'], genome['hardcoded'] = genome['hardcoded'], genome['random']
        return genome

    def crossover(self, genome_1, genome_2):
        '''Crossover function'''

        return  self.control_thresholds(
            {
                # Average crossover
                'random': (genome_1['random']+genome_2['random'])*0.5,
                'hardcoded': (genome_1['hardcoded']+genome_2['hardcoded'])*0.5,
                'mcts': (genome_1['mcts']+genome_2['mcts'])*0.5,
                'fitness': genome_1['fitness'],
            })

    def mutation(self, genome):
        '''Mutation function'''

        while random.random() < .4:
            genome['random'] = random.random()*GENOME_VAL_UPPER_BOUND
            genome['hardcoded'] = genome['random'] + random.random()*(GENOME_VAL_UPPER_BOUND-genome['random'])
            genome['mcts'] = genome['hardcoded'] + random.random()*(GENOME_VAL_UPPER_BOUND-genome['hardcoded'])

        return self.control_thresholds(genome)
        
    def evolution(self):
        '''Trains the genomes using evolutionary strategies'''

        # Initialize population
        populat = [dict() for _ in range(self._population_size)]
        for p in populat:
            p['random'] = random.random()*GENOME_VAL_UPPER_BOUND
            p['hardcoded'] = p['random'] + random.random()*(GENOME_VAL_UPPER_BOUND-p['random'])
            p['mcts'] = p['hardcoded'] + random.random()*(GENOME_VAL_UPPER_BOUND-p['hardcoded'])
            p['fitness'] = 0.0
        population = [self.control_thresholds(g) for g in populat]
        
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
                else:
                    # Crossover
                    new_genome = self.crossover(selected_1, selected_2)
                
                win = self.game(new_genome) # Game simulation with a certain set of parameters
                new_fitness = win/self._games_to_play # New fitness
                offspring.append({
                    'random': new_genome['random'],
                    'hardcoded': new_genome['hardcoded'],
                    'mcts': new_genome['mcts'],
                    'fitness': new_fitness
                })

            population += offspring
            population = sorted(population, key=lambda i: i['fitness'], reverse=True)[:self._population_size]

        # When all loops over generations are out, store the best genome
        with open('./GAPlayer/parameters.json', 'w') as fp:
            fp.write(json.dumps([population[0]['random'], population[0]['hardcoded'], population[0]['mcts']]))
        return population[0]['random'], population[0]['hardcoded'], population[0]['mcts']