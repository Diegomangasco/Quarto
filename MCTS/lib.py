from .quartoTrain import *

class UsefulFunctions(object):
    '''Defines useful function for the training'''

    def __init__(self) -> None:
        pass

    def equal_boards(self, board_1, board_2):
        '''Compares two boards'''

        for x in range(0, 3):
            for j in range(0, 3):
                if board_1[j, x] != board_2[j, x]:
                    return False

        return True

    def free_pieces_and_places(self, state: QuartoTrain):
        '''Returns all possible free pieces and places for the current state'''

        board = state.get_board_status()
        free_pieces = [piece for piece in range(0, 16) if piece not in board]
        free_places = [(i, j) for i in range(0, 4) for j in range(0, 4) if board[j, i] == -1]
        
        return free_pieces, free_places

    def do_one_random_step(self, state: QuartoTrain):
        '''Does one random game beginning on the current state to create another one'''

        free_pieces, free_places = self.free_pieces_and_places(state)
        piece, place = state.run(free_pieces, free_places) # Run only one move to create a new state
        return state, piece, place

    def simulate_game(self, state: QuartoTrain):
        '''Simulates a game untill the end'''

        free_pieces, free_places = self.free_pieces_and_places(state)
        winner = state.run(free_pieces, free_places, single=False)
        return winner