import random
import quarto
import numpy as np

class HardcodedFunctions():

    def __init__(self) -> None:
        pass

    def find_piece(self, quarto: quarto.Quarto):
        '''Finds a good piece to choose for the opponent'''

        state = quarto
        board = state.get_board_status()

        free_pieces = {(piece, state.get_piece_charachteristics(piece)) for piece in range(0, 16) if piece not in board}
        avoid_pieces = set()

        # Check all the rows triplets

        for i in range(state.BOARD_SIDE):
            if board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] == -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 1])
                piece_3 = state.get_piece_charachteristics(board[i, 2])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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

        for i in range(state.BOARD_SIDE):
            if board[0, i] != -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] == -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[1, i])
                piece_3 = state.get_piece_charachteristics(board[2, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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

        if board[0, 0] != -1 and board[1, 1] != -1 and board[2, 2] != -1 and board[3, 3] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, 0])
            piece_2 = state.get_piece_charachteristics(board[1, 1])
            piece_3 = state.get_piece_charachteristics(board[2, 2])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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

        if board[0, 3] != -1 and board[1, 2] != -1 and board[2, 1] != -1 and board[3, 0] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, 3])
            piece_2 = state.get_piece_charachteristics(board[1, 2])
            piece_3 = state.get_piece_charachteristics(board[2, 1])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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
            piece_1 = state.get_piece_charachteristics(board[1, 2])
            piece_2 = state.get_piece_charachteristics(board[0, 3])
            piece_3 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                    for piece in free_pieces:
                        if piece[1].HIGH == True:
                            avoid_pieces.add(piece[0])
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
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

        free_pieces = {piece[0] for piece in free_pieces}
        free_pieces_available = free_pieces - avoid_pieces
        if len(free_pieces_available) != 0:
            return random.choice(list(free_pieces_available))
        else:
            return random.choice(list(free_pieces))

    def find_position(self, quarto: quarto.Quarto):
        '''Finds the first 'hot' position where our agent can place a piece'''

        state = quarto
        board = state.get_board_status()
        piece_to_place = state.get_piece_charachteristics(state.get_selected_piece())

        # Check all the rows triplets

        for i in range(state.BOARD_SIDE):
            if board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] == -1:
                piece_1 = state.get_piece_charachteristics(board[i, 0])
                piece_2 = state.get_piece_charachteristics(board[i, 1])
                piece_3 = state.get_piece_charachteristics(board[i, 2])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return i, 3
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
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
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
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
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
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
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                    return i, 2
                if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                    return i, 2
                if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SQUARE == True:
                    return i, 2

        # Check all the columns triplets 

        for i in range(state.BOARD_SIDE):
            if board[0, i] != -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] == -1:
                piece_1 = state.get_piece_charachteristics(board[0, i])
                piece_2 = state.get_piece_charachteristics(board[1, i])
                piece_3 = state.get_piece_charachteristics(board[2, i])
                if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                    return 3, i
                if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
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
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True and piece_to_place.HIGH == True:
                return 1, 1
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True and piece_to_place.COLOURED == True:
                return 1, 1
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True and piece_to_place.SQUARE == True:
                return 1, 1
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True and piece_to_place.SOLID == True:
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
            piece_1 = state.get_piece_charachteristics(board[1, 2])
            piece_2 = state.get_piece_charachteristics(board[0, 3])
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

        # Check all columns couples

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

        # Check all first diagonal couples

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

        # Check all second diagonal couples

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
        if board[0, 0] == -1 and board[1, 2] == -1 and board[2, 1] != -1 and board[3, 0] != -1:
            piece_1 = state.get_piece_charachteristics(board[2, 1])
            piece_2 = state.get_piece_charachteristics(board[3, 0])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True and piece_to_place.HIGH == True:
                return random.choice([(0, 0), (1, 2)])
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True and piece_to_place.COLOURED == True:
                return random.choice([(0, 0), (1, 2)])
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True and piece_to_place.SQUARE == True:
                return random.choice([(0, 0), (1, 2)])
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True and piece_to_place.SOLID == True:
                return random.choice([(0, 0), (1, 2)])

        # If no opportunity was found, play random
        return random.choice([(i, j) for i in range(0, 4) for j in range(0, 4) if board[i, j] == -1])
        
