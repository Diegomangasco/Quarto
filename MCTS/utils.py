import numpy as np
from .quartoTrain import *

class UsefulFunctions(object):
    '''Defines useful function for the training'''

    def __init__(self) -> None:
        pass

    def symmetries(self, board):
        '''Defines four boards that could be equivalent to the original one'''

        rotate_90_clockwise = np.rot90(board)
        rotate_90_counter_clockwise = np.rot90(board, k=3)
        reflect_horizontal = np.fliplr(board)
        reflect_vertical = np.flipud(board)

        return rotate_90_clockwise, rotate_90_counter_clockwise, reflect_horizontal, reflect_vertical

    def free_places(self, state: QuartoTrain):
        '''Returns all possible free places for the current state'''

        board = state.get_board_status()
        free_places = [(j, i) for i in range(0, 4) for j in range(0, 4) if board[j, i] == -1]
        
        return free_places
            
    def free_pieces(self, state: QuartoTrain):
        '''Returns all possible free pieces for the current state'''

        board = state.get_board_status()
        free_pieces = [piece for piece in range(0, 16) if piece not in board]
        
        return free_pieces

    def simulate_game(self, state: QuartoTrain, player_id: int):
        '''Simulates a game untill the end'''

        while True:
            if state.check_finished() or state.check_winner() != -1:
                if state.check_winner() == player_id:
                    reward = 1  
                elif state.check_winner() == -1:
                    reward = .5
                else:
                    reward = 0 
                return reward
            free_pieces = self.free_pieces(state)
            free_places = self.free_places(state)
            state.run(free_pieces, free_places)