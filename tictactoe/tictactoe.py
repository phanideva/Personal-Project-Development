"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}



def result(board, action):
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combination in winning_combinations:
        if all(board[i][j] == X for i, j in combination):
            return X
        if all(board[i][j] == O for i, j in combination):
            return O
    return None


def terminal(board):
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move

def max_value(board):
    if terminal(board):
        return utility(board), None
    v = float("-inf")
    move = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v, move = min_val, action
    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float("inf")
    move = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v, move = max_val, action
    return v, move

