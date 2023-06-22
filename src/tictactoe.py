from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_board():
    """
    Returns initial state of board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns which player's turn it is.
    """
    sum_O = 0
    sum_X = 0
    if not any(X in y for y in board):
        return X

    for i in board:
        sum_O += i.count(O)
        sum_X += i.count(X)

    if sum_O < sum_X:
        return O
    else:
        return X


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Unvalid move!")

    board_copy = deepcopy(board)

    if player(board) == X:
        board_copy[action[0]][action[1]] = X
    else:
        board_copy[action[0]][action[1]] = O

    return board_copy


def winner(board):
    """
    Returns the winner, else return None
    """
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]

    if [X, X, X] in (board[0], board[1], board[2]):
        return X
    if [X, X, X] in ([row[0] for row in board], [row[1] for row in board], [row[2] for row in board]):
        return X
    if [X, X, X] in (diag1, diag2):
        return X

    if [O, O, O] in (board[0], board[1], board[2]):
        return O
    if [O, O, O] in ([row[0] for row in board], [row[1] for row in board], [row[2] for row in board]):
        return O
    if [O, O, O] in (diag1, diag2):
        return O

    return None


def game_over(board):
    """
    Returns True if game is over, else returns False.
    """
    if winner(board) is not None or (EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]):
        return True
    else:
        return False


def actions(board):
    """
    Returns set of all possible actions.
    """
    valid_moves = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                valid_moves.add((i,j))

    return valid_moves

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) is None:
        return 0


def minimax(board):
    """
    Returns best possible move using the minimax algorithm.
    """
    if game_over(board):
        return None

    def max_value(board):
        v = -2
        if game_over(board):
            return utility(board)
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        v = 2
        if game_over(board):
            return utility(board)
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if player(board) == X:
        for action in actions(board):
            if max_value(board) == min_value(result(board,action)):
                return action

    if player(board) == O:
        for action in actions(board):
            if min_value(board) == max_value(result(board,action)):
                return action
