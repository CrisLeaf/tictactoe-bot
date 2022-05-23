import numpy as np


def check_win(board, piece):
    for row in board:
        if sum(row) == 3 * piece:
            return True

    for col in np.transpose(board):
        if sum(col) == 3 * piece:
            return True

    if sum([board[i][i] for i in range(3)]) == 3 * piece:
        return True

    if sum([board[i][2-i] for i in range(3)]) == 3 * piece:
        return True

    return False

def check_draw(board):
    zeros = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                zeros += 1

    if zeros > 0:
        return False
    elif check_win(board, 1) or check_win(board, -1):
            return False
    else:
        return True

def is_valid_position(board, i, j):
    if board[i][j] == 0:
        return True
    else:
        return False

def get_valid_positions(board):
    positions = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                positions.append(str(i) + str(j))

    return positions

def check_second_turn(board):
    positives = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                positives += 1

    if positives == 1:
        return True

def last_turn(board):
    zeros = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False

    return True

def minimax(board, next_piece, maximizing, first, iter):
    iter += 1

    if check_draw(board):
        return 0
    elif check_win(board, -1):
        return 1 * (10 - iter)
    elif check_win(board, 1):
        return -1 * (10 - iter)

    scores = []
    for i in range(3):
        for j in range(3):
            if is_valid_position(board, i, j):
                board[i][j] = next_piece

                scores.append(minimax(board, -1 * next_piece, not maximizing, False, iter))
                board[i][j] = 0

    if first:
        return scores
    else:
        return max(scores) if maximizing else min(scores)

def next_move(board, next_piece):
    if check_second_turn(board):
        if board[1][1] == 0:
            return "11"
        else:
            return np.random.choice(["00", "02", "20", "22"], 1)[0]

    else:
        move = minimax(board, next_piece, True, True, 0)
        max_index = move.index(max(move))
        positions = get_valid_positions(board)

        return positions[max_index]
