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
