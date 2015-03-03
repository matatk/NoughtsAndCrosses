def test_legal_move_is_legal():
    move = 0
    assert is_legal(move)


def test_illegal_move_is_not_legal():
    move = -1
    assert is_legal(move) is False


def test_different_legal_move_is_legal():
    move = 1
    assert is_legal(move)


def is_legal(move):
    return move == 0 or move > 0
