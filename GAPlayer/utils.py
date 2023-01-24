from MCTS.quartoTrain import *

def board_score(self, state: QuartoTrain):
        '''Computes a score for the board, basing on the number of couples and triplets'''

        positions = {
            'singles': 0,
            'couples': 0,
            'triplets': 0,
        }

        board = state.get_board_status()
        row_done = [False, False, False, False]
        for i in range(state.BOARD_SIDE):
            column_done = False
            diagonal_done = False
            for j in range(state.BOARD_SIDE):

                if board[j, i] != -1:
                    positions['singles'] += 1
                    if not column_done and j+2 < state.BOARD_SIDE and board[j+1, i] != -1 and board[j+2, i] != -1 and ((j+3 < state.BOARD_SIDE and board[j+3, i] == -1) or (j-1 > 0 and board[j-1, i] == -1)):
                        piece_1 = state.get_piece_charachteristics(board[j, i])
                        piece_2 = state.get_piece_charachteristics(board[j+1, i])
                        piece_3 = state.get_piece_charachteristics(board[j+2, i])
                        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                            positions['triplets'] += 1
                            column_done = True
                        if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                            positions['triplets'] += 1
                            column_done = True
                        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                            positions['triplets'] += 1
                            column_done = True
                        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                            positions['triplets'] += 1
                            column_done = True
                    if not column_done and j+1 < state.BOARD_SIDE and board[j+1, i] != -1 and ((j+2 < state.BOARD_SIDE and board[j+2, i] == -1 and j+3 < state.BOARD_SIDE and board[j+3, i] == -1) or (j-1 > 0 and board[j-1, i] == -1 and j+2 < state.BOARD_SIDE and board[j+2, i] == -1) or (j-1 > 0 and board[j-1, i] == -1 and j-2 > 0 and board[j-2, i] == -1)):
                        piece_1 = state.get_piece_charachteristics(board[j, i])
                        piece_2 = state.get_piece_charachteristics(board[j+1, i])
                        if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                            positions['couples'] += 1
                        if piece_1.HIGH == piece_2.COLOURED and piece_1.COLOURED == True:
                            positions['couples'] += 1
                        if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                            positions['couples'] += 1
                        if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                            positions['couples'] += 1

                    if not row_done[i] and i+2 < state.BOARD_SIDE and board[j, i+1] != -1 and board[j, i+2] != -1 and ((i+3 < state.BOARD_SIDE and board[j, i+3] == -1) or (i-1 > 0 and board[j, i-1] == -1)):
                        piece_1 = state.get_piece_charachteristics(board[j, i])
                        piece_2 = state.get_piece_charachteristics(board[j, i+1])
                        piece_3 = state.get_piece_charachteristics(board[j, i+2])
                        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                            positions['triplets'] += 1
                            row_done = True
                        if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                            positions['triplets'] += 1
                            row_done = True
                        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                            positions['triplets'] += 1
                            row_done = True
                        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                            positions['triplets'] += 1
                            row_done = True
                    if not row_done and i+1 < state.BOARD_SIDE and board[j, i+1] != -1 and ((i+2 < state.BOARD_SIDE and board[j, i+2] == -1 and i+3 < state.BOARD_SIDE and board[j, i+3] == -1) or (i-1 > 0 and board[j, i-1] == -1 and i+2 < state.BOARD_SIDE and board[j, i+2] == -1) or (i-1 > 0 and board[j, i-1] == -1 and i-2 > 0 and board[j, i-2] == -1)):
                        piece_1 = state.get_piece_charachteristics(board[j, i])
                        piece_2 = state.get_piece_charachteristics(board[j, i+1])
                        if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                            positions['couples'] += 1
                            row_done = True
                        if piece_1.HIGH == piece_2.COLOURED and piece_1.COLOURED == True:
                            positions['couples'] += 1
                            row_done = True
                        if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                            positions['couples'] += 1
                            row_done = True
                        if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                            positions['couples'] += 1
                            row_done = True