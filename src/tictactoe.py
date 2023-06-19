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
    Returns True if game is over, else returns False
    """
    if winner(board) is not None or (EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]):
        return True
    else:
        return False
