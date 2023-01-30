import random
import quarto
import numpy as np

class HardcodedFunctions():

    def __init__(self) -> None:
        pass

    def find_piece(self, quarto: quarto.Quarto):
        '''Finds a good piece to choose for the opponent.\n
        This function uses one set for the free pieces (with index and characteristics of each piece) 
        that are outside the board (i.e. not yet placed), and another one to collect pieces 
        that must be avoided in the selection. \n
        The metric to choose if a piece must be avoided, is to control if that piece will lead to a win for the opponent. \n
        In particular, the function checks all rows, columns and diagonals when there can be a triplets 
        and checks which characteristic the piece should have to compute a win combination for the triplet. \n
        If a winning piece is present in the set of free pieces, it adds it to the set of the avoid pieces to not choose it. \n
        At the end, when all rows, columns and diagonals have been checked, a new set in created 
        by making a difference between the two sets. \n
        Then a random possible piece is returned from this new set. \n
        If the new set is empty, a random piece is returned from the free pieces set.'''

        state = quarto
        board = state.get_board_status()

        free_pieces = {(piece, state.get_piece_charachteristics(piece)) for piece in range(0, 16) if piece not in board}
        avoid_pieces = set()

        # Check all the rows triplets
        # Loop over all the rows and update the avoid_pieces set
        for i in range(state.BOARD_SIDE):
            if board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] == -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 1])
                piece_3 = state.get_piece_charachteristics(board[i, 2])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                    for piece in free_pieces:
                        if piece[1].COLOURED == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                    for piece in free_pieces:
                        if piece[1].SQUARE == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                    for piece in free_pieces:
                        if piece[1].SOLID == True:
                            avoid_pieces.add(piece[0])
            if board[i, 0] == -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] != -1:
                piece_1 = state.get_piece_charachteristics(board[i, 1])
                piece_2 = state.get_piece_charachteristics(board[i, 2])
                piece_3 = state.get_piece_charachteristics(board[i, 3])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                    for piece in free_pieces:
                        if piece[1].COLOURED == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                    for piece in free_pieces:
                        if piece[1].SQUARE == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                    for piece in free_pieces:
                        if piece[1].SOLID == True:
                            avoid_pieces.add(piece[0])
            if board[i, 0] != -1 and board[i, 1] == -1 and board[i, 2] != -1 and board[i, 3] != -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 2])
                piece_3 = state.get_piece_charachteristics(board[i, 3])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                    for piece in free_pieces:
                        if piece[1].COLOURED == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                    for piece in free_pieces:
                        if piece[1].SQUARE == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                    for piece in free_pieces:
                        if piece[1].SOLID == True:
                            avoid_pieces.add(piece[0])
            if board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] == -1 and board[i, 3] != -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 1])
                piece_3 = state.get_piece_charachteristics(board[i, 3])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                    for piece in free_pieces:
                        if piece[1].COLOURED == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                    for piece in free_pieces:
                        if piece[1].SQUARE == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                    for piece in free_pieces:
                        if piece[1].SOLID == True:
                            avoid_pieces.add(piece[0])

        # Check all the columns triplets 
        # Loop over all the columnss and update the avoid_pieces set
        for i in range(state.BOARD_SIDE):
            if board[0, i] != -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] == -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[1, i])
                piece_3 = state.get_piece_charachteristics(board[2, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                    for piece in free_pieces:
                        if piece[1].COLOURED == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                    for piece in free_pieces:
                        if piece[1].SQUARE == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                    for piece in free_pieces:
                        if piece[1].SOLID == True:
                            avoid_pieces.add(piece[0])
            if board[0, i] == -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] != -1:
                piece_1 = state.get_piece_charachteristics(board[1, i])
                piece_2 = state.get_piece_charachteristics(board[2, i])
                piece_3 = state.get_piece_charachteristics(board[3, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                    for piece in free_pieces:
                        if piece[1].COLOURED == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                    for piece in free_pieces:
                        if piece[1].SQUARE == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                    for piece in free_pieces:
                        if piece[1].SOLID == True:
                            avoid_pieces.add(piece[0])
            if board[0, i] != -1 and board[1, i] == -1 and board[2, i] != -1 and board[3, i] != -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[2, i])
                piece_3 = state.get_piece_charachteristics(board[3, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                    for piece in free_pieces:
                        if piece[1].COLOURED == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                    for piece in free_pieces:
                        if piece[1].SQUARE == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                    for piece in free_pieces:
                        if piece[1].SOLID == True:
                            avoid_pieces.add(piece[0])
            if board[0, i] != -1 and board[1, i] != -1 and board[2, i] == -1 and board[3, i] != -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[1, i])
                piece_3 = state.get_piece_charachteristics(board[3, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                    for piece in free_pieces:
                        if piece[1].COLOURED == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                    for piece in free_pieces:
                        if piece[1].SQUARE == True:
                            avoid_pieces.add(piece[0])
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                    for piece in free_pieces:
                        if piece[1].SOLID == True:
                            avoid_pieces.add(piece[0])

        # Check first diagonal triplets
        # Don't use loop, I prefer to make a more precise and clearer strategy
        if board[0, 0] != -1 and board[1, 1] != -1 and board[2, 2] != -1 and board[3, 3] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, 0])
            piece_2 = state.get_piece_charachteristics(board[1, 1])
            piece_3 = state.get_piece_charachteristics(board[2, 2])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                for piece in free_pieces:
                    if piece[1].COLOURED == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                for piece in free_pieces:
                    if piece[1].SQUARE == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                for piece in free_pieces:
                    if piece[1].SOLID == True:
                        avoid_pieces.add(piece[0])
        if board[0, 0] == -1 and board[1, 1] != -1 and board[2, 2] != -1 and board[3, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[1, 1])
            piece_2 = state.get_piece_charachteristics(board[2, 2])
            piece_3 = state.get_piece_charachteristics(board[3, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                for piece in free_pieces:
                    if piece[1].COLOURED == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                for piece in free_pieces:
                    if piece[1].SQUARE == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                for piece in free_pieces:
                    if piece[1].SOLID == True:
                        avoid_pieces.add(piece[0])
        if board[0, 0] != -1 and board[1, 1] == -1 and board[2, 2] != -1 and board[3, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 0])
            piece_2 = state.get_piece_charachteristics(board[2, 2])
            piece_3 = state.get_piece_charachteristics(board[3, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                for piece in free_pieces:
                    if piece[1].COLOURED == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                for piece in free_pieces:
                    if piece[1].SQUARE == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                for piece in free_pieces:
                    if piece[1].SOLID == True:
                        avoid_pieces.add(piece[0])
        if board[0, 0] != -1 and board[1, 1] != -1 and board[2, 2] == -1 and board[3, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 0])
            piece_2 = state.get_piece_charachteristics(board[1, 1])
            piece_3 = state.get_piece_charachteristics(board[3, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                for piece in free_pieces:
                    if piece[1].COLOURED == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                for piece in free_pieces:
                    if piece[1].SQUARE == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                for piece in free_pieces:
                    if piece[1].SOLID == True:
                        avoid_pieces.add(piece[0])

        # Check second diagonal triplets
        # Don't use loop, I prefer to make a more precise and clearer strategy
        if board[0, 3] != -1 and board[1, 2] != -1 and board[2, 1] != -1 and board[3, 0] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, 3])
            piece_2 = state.get_piece_charachteristics(board[1, 2])
            piece_3 = state.get_piece_charachteristics(board[2, 1])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                for piece in free_pieces:
                    if piece[1].COLOURED == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                for piece in free_pieces:
                    if piece[1].SQUARE == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                for piece in free_pieces:
                    if piece[1].SOLID == True:
                        avoid_pieces.add(piece[0])
        if board[0, 3] == -1 and board[1, 2] != -1 and board[2, 1] != -1 and board[3, 0] != -1:
            piece_1 = state.get_piece_charachteristics(board[1, 2])
            piece_2 = state.get_piece_charachteristics(board[2, 1])
            piece_3 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                for piece in free_pieces:
                    if piece[1].COLOURED == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                for piece in free_pieces:
                    if piece[1].SQUARE == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                for piece in free_pieces:
                    if piece[1].SOLID == True:
                        avoid_pieces.add(piece[0])
        if board[0, 3] != -1 and board[1, 2] == -1 and board[2, 1] != -1 and board[3, 0] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 3])
            piece_2 = state.get_piece_charachteristics(board[2, 1])
            piece_3 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                for piece in free_pieces:
                    if piece[1].COLOURED == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                for piece in free_pieces:
                    if piece[1].SQUARE == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                for piece in free_pieces:
                    if piece[1].SOLID == True:
                        avoid_pieces.add(piece[0])
        if board[0, 3] != -1 and board[1, 2] != -1 and board[2, 1] == -1 and board[3, 0] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 3])
            piece_2 = state.get_piece_charachteristics(board[1, 2])
            piece_3 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                for piece in free_pieces:
                    if piece[1].COLOURED == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                for piece in free_pieces:
                    if piece[1].SQUARE == True:
                        avoid_pieces.add(piece[0])
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                for piece in free_pieces:
                    if piece[1].SOLID == True:
                        avoid_pieces.add(piece[0])

        # Keep only the indexes of the free pieces
        free_pieces = {piece[0] for piece in free_pieces}
        free_pieces_available = free_pieces - avoid_pieces # Available and not dangerous pieces
        if len(free_pieces_available) != 0:
            return random.choice(list(free_pieces_available))
        else:
            # If we don't have available and not dangerous pieces we are forced to play randomly
            return random.choice(list(free_pieces))  

    def find_position(self, quarto: quarto.Quarto):
        '''Finds the first 'hot' position where our agent can place a piece. \n
        This function checks through all the board if the piece selected by the opponent could be placed 
        in a good position for the agent. \n
        In particular a control of the triplets is done first, over all rows, columns and diagonals. \n
        If one of the triplets checked can be completed by the current piece (i.e. the current piece has a 
        characteristic that also the other three pieces in the triplets have), it is returned. \n
        After triplets checks, the function performs a control for the couples over all rows, columns and diagonals 
        and if a triplet can be made, on of the two possible positions 
        (for a possible winning game, the couple must have two free positions in its line), 
        chosen randomly, is returned. \n
        If no place is found, the function returns a random free position.'''

        state = quarto
        board = state.get_board_status()
        piece_to_place = state.get_piece_charachteristics(state.get_selected_piece())

        # Check all the rows triplets
        # If a winning position is found, return it
        for i in range(state.BOARD_SIDE):
            if board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] == -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 1])
                piece_3 = state.get_piece_charachteristics(board[i, 2])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return i, 3
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return i, 3
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return i, 3
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SQUARE == True:
                    return i, 3
            if board[i, 0] == -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] != -1:
                piece_1 = state.get_piece_charachteristics(board[i, 1])
                piece_2 = state.get_piece_charachteristics(board[i, 2])
                piece_3 = state.get_piece_charachteristics(board[i, 3])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return i, 0
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return i, 0
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return i, 0
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SQUARE == True:
                    return i, 0
            if board[i, 0] != -1 and board[i, 1] == -1 and board[i, 2] != -1 and board[i, 3] != -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 2])
                piece_3 = state.get_piece_charachteristics(board[i, 3])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return i, 1
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return i, 1
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return i, 1
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SQUARE == True:
                    return i, 1
            if board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] == -1 and board[i, 3] != -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 1])
                piece_3 = state.get_piece_charachteristics(board[i, 3])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return i, 2
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return i, 2
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return i, 2
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SQUARE == True:
                    return i, 2

        # Check all the columns triplets 
        # If a winning position is found, return it
        for i in range(state.BOARD_SIDE):
            if board[0, i] != -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] == -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[1, i])
                piece_3 = state.get_piece_charachteristics(board[2, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return 3, i
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return 3, i
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return 3, i
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return 3, i
            if board[0, i] == -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] != -1:
                piece_1 = state.get_piece_charachteristics(board[1, i])
                piece_2 = state.get_piece_charachteristics(board[2, i])
                piece_3 = state.get_piece_charachteristics(board[3, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return 0, i
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return 0, i
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return 0, i
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return 0, i
            if board[0, i] != -1 and board[1, i] == -1 and board[2, i] != -1 and board[3, i] != -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[2, i])
                piece_3 = state.get_piece_charachteristics(board[3, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return 1, i
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return 1, i
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return 1, i
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return 1, i
            if board[0, i] != -1 and board[1, i] != -1 and board[2, i] == -1 and board[3, i] != -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[1, i])
                piece_3 = state.get_piece_charachteristics(board[3, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return 2, i
                if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return 2, i
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return 2, i
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return 2, i

        # Check first diagonal triplets
        # If a winning position is found, return it
        if board[0, 0] != -1 and board[1, 1] != -1 and board[2, 2] != -1 and board[3, 3] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, 0])
            piece_2 = state.get_piece_charachteristics(board[1, 1])
            piece_3 = state.get_piece_charachteristics(board[2, 2])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return 3, 3
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return 3, 3
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return 3, 3
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return 3, 3
        if board[0, 0] == -1 and board[1, 1] != -1 and board[2, 2] != -1 and board[3, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[1, 1])
            piece_2 = state.get_piece_charachteristics(board[2, 2])
            piece_3 = state.get_piece_charachteristics(board[3, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return 0, 0
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return 0, 0
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return 0, 0
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return 0, 0
        if board[0, 0] != -1 and board[1, 1] == -1 and board[2, 2] != -1 and board[3, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 0])
            piece_2 = state.get_piece_charachteristics(board[2, 2])
            piece_3 = state.get_piece_charachteristics(board[3, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return 1, 1
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return 1, 1
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return 1, 1
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return 1, 1
        if board[0, 0] != -1 and board[1, 1] != -1 and board[2, 2] == -1 and board[3, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 0])
            piece_2 = state.get_piece_charachteristics(board[1, 1])
            piece_3 = state.get_piece_charachteristics(board[3, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return 2, 2
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return 2, 2
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return 2, 2
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return 2, 2

        # Check second diagonal triplets
        # If a winning position is found, return it
        if board[0, 3] != -1 and board[1, 2] != -1 and board[2, 1] != -1 and board[3, 0] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, 3])
            piece_2 = state.get_piece_charachteristics(board[1, 2])
            piece_3 = state.get_piece_charachteristics(board[2, 1])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return 3, 0
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return 3, 0
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return 3, 0
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return 3, 0
        if board[0, 3] == -1 and board[1, 2] != -1 and board[2, 1] != -1 and board[3, 0] != -1:
            piece_1 = state.get_piece_charachteristics(board[1, 2])
            piece_2 = state.get_piece_charachteristics(board[2, 1])
            piece_3 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return 0, 3
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return 0, 3
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return 0, 3
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return 0, 3
        if board[0, 3] != -1 and board[1, 2] == -1 and board[2, 1] != -1 and board[3, 0] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 3])
            piece_2 = state.get_piece_charachteristics(board[2, 1])
            piece_3 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return 1, 2
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return 1, 2
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return 1, 2
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return 1, 2
        if board[0, 3] != -1 and board[1, 2] != -1 and board[2, 1] == -1 and board[3, 0] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 3])
            piece_2 = state.get_piece_charachteristics(board[1, 2])
            piece_3 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return 2, 1
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return 2, 1
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return 2, 1
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return 2, 1

        # Check all rows couples
        # If a position can make a winning triplet, return it
        for i in range(state.BOARD_SIDE):
            if board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] == -1 and board[i, 3] == -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 1])
                if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return random.choice([(i, 2), (i, 3)])
                if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return random.choice([(i, 2), (i, 3)])
                if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return random.choice([(i, 2), (i, 3)])
                if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return random.choice([(i, 2), (i, 3)])
            if board[i, 0] == -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] == -1:
                piece_1 = state.get_piece_charachteristics(board[i, 1])
                piece_2 = state.get_piece_charachteristics(board[i, 2])
                if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return random.choice([(i, 0), (i, 3)])
                if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return random.choice([(i, 0), (i, 3)])
                if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return random.choice([(i, 0), (i, 3)])
                if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return random.choice([(i, 0), (i, 3)])
            if board[i, 0] == -1 and board[i, 1] == -1 and board[i, 2] != -1 and board[i, 3] != -1:
                piece_1 = state.get_piece_charachteristics(board[i, 2])
                piece_2 = state.get_piece_charachteristics(board[i, 3])
                if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return random.choice([(i, 0), (i, 1)])
                if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return random.choice([(i, 0), (i, 1)])
                if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return random.choice([(i, 0), (i, 1)])
                if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return random.choice([(i, 0), (i, 1)])
            if board[i, 0] != -1 and board[i, 1] == -1 and board[i, 2] == -1 and board[i, 3] != -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 3])
                if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return random.choice([(i, 1), (i, 2)])
                if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return random.choice([(i, 1), (i, 2)])
                if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return random.choice([(i, 1), (i, 2)])
                if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return random.choice([(i, 1), (i, 2)])

        # Check all columns couples
        # If a position can make a winning triplet, return it
        for i in range(state.BOARD_SIDE):
            if board[0, i] != -1 and board[1, i] != -1 and board[2, i] == -1 and board[3, i] == -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[1, i])
                if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return random.choice([(2, i), (3, i)])
                if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return random.choice([(2, i), (3, i)])
                if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return random.choice([(2, i), (3, i)])
                if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return random.choice([(2, i), (3, i)])
            if board[0, i] == -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] == -1:
                piece_1 = state.get_piece_charachteristics(board[1, i])
                piece_2 = state.get_piece_charachteristics(board[2, i])
                if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return random.choice([(0, i), (3, i)])
                if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return random.choice([(0, i), (3, i)])
                if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return random.choice([(0, i), (3, i)])
                if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return random.choice([(0, i), (3, i)])
            if board[0, i] == -1 and board[1, i] == -1 and board[2, i] != -1 and board[3, i] != -1:
                piece_1 = state.get_piece_charachteristics(board[2, i])
                piece_2 = state.get_piece_charachteristics(board[3, i])
                if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return random.choice([(0, i), (1, i)])
                if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return random.choice([(0, i), (1, i)])
                if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return random.choice([(0, i), (1, i)])
                if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return random.choice([(0, i), (1, i)])
            if board[0, i] != -1 and board[1, i] == -1 and board[2, i] == -1 and board[3, i] != -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[3, i])
                if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return random.choice([(1, i), (2, i)])
                if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return random.choice([(1, i), (2, i)])
                if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return random.choice([(1, i), (2, i)])
                if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                    return random.choice([(1, i), (2, i)])

        # Check all first diagonal couples
        # If a position can make a winning triplet, return it
        if board[0, 0] != -1 and board[1, 1] != -1 and board[2, 2] == -1 and board[3, 3] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, 0])
            piece_2 = state.get_piece_charachteristics(board[1, 1])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return random.choice([(2, 2), (3, 3)])
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return random.choice([(2, 2), (3, 3)])
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return random.choice([(2, 2), (3, 3)])
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return random.choice([(2, 2), (3, 3)])
        if board[0, 0] == -1 and board[1, 1] != -1 and board[2, 2] != -1 and board[3, 3] == -1:
            piece_1 = state.get_piece_charachteristics(board[1, 1])
            piece_2 = state.get_piece_charachteristics(board[2, 2])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return random.choice([(0, 0), (3, 3)])
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return random.choice([(0, 0), (3, 3)])
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return random.choice([(0, 0), (3, 3)])
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return random.choice([(0, 0), (3, 3)])
        if board[0, 0] == -1 and board[1, 1] == -1 and board[2, 2] != -1 and board[3, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[2, 2])
            piece_2 = state.get_piece_charachteristics(board[3, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return random.choice([(0, 0), (1, 1)])
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return random.choice([(0, 0), (1, 1)])
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return random.choice([(0, 0), (1, 1)])
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return random.choice([(0, 0), (1, 1)])
        if board[0, 0] != -1 and board[1, 1] == -1 and board[2, 2] == -1 and board[3, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 0])
            piece_2 = state.get_piece_charachteristics(board[3, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return random.choice([(1, 1), (2, 2)])
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return random.choice([(1, 1), (2, 2)])
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return random.choice([(1, 1), (2, 2)])
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return random.choice([(1, 1), (2, 2)])

        # Check all second diagonal couples
        # If a position can make a winning triplet, return it
        if board[0, 3] != -1 and board[1, 2] != -1 and board[2, 1] == -1 and board[3, 0] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, 3])
            piece_2 = state.get_piece_charachteristics(board[1, 2])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return random.choice([(2, 1), (3, 0)])
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return random.choice([(2, 1), (3, 0)])
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return random.choice([(2, 1), (3, 0)])
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return random.choice([(2, 1), (3, 0)])
        if board[0, 3] == -1 and board[1, 2] != -1 and board[2, 1] != -1 and board[3, 0] == -1:
            piece_1 = state.get_piece_charachteristics(board[1, 2])
            piece_2 = state.get_piece_charachteristics(board[2, 1])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return random.choice([(0, 3), (3, 0)])
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return random.choice([(0, 3), (3, 0)])
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return random.choice([(0, 3), (3, 0)])
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return random.choice([(0, 3), (3, 0)])
        if board[0, 3] == -1 and board[1, 2] == -1 and board[2, 1] != -1 and board[3, 0] != -1:
            piece_1 = state.get_piece_charachteristics(board[2, 1])
            piece_2 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return random.choice([(0, 3), (1, 2)])
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return random.choice([(0, 3), (1, 2)])
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return random.choice([(0, 3), (1, 2)])
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return random.choice([(0, 3), (1, 2)])
        if board[0, 3] != -1 and board[1, 2] == -1 and board[2, 1] == -1 and board[3, 0] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, 3])
            piece_2 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return random.choice([(2, 1), (1, 2)])
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return random.choice([(2, 1), (1, 2)])
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return random.choice([(2, 1), (1, 2)])
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return random.choice([(2, 1), (1, 2)])

        # If no opportunity was found, play random
        return random.choice([(i, j) for i in range(0, 4) for j in range(0, 4) if board[i, j] == -1])
        
