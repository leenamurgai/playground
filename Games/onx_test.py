from collections import Counter
from onx import board

def test_get_board():
    my_board = board()
    assert my_board.get_board() == [['-', '-', '-'],
                                    ['-', '-', '-'],
                                    ['-', '-', '-']]

def test_set_board():
    list_board = [['-', '-', 'x'],
                  ['-', 'x', '-'],
                  ['x', '-', '-']]
    my_board = board()
    my_board.set_board(list_board)
    assert my_board.get_board() == list_board

def test_display_board():
    my_board = board()
    assert my_board.display_board() == ['-|-|-']*3

def test_is_full():
    list_board = [['-', '-', 'x'],
                  ['-', 'x', '-'],
                  ['x', '-', '-']]
    my_board = board()
    my_board.set_board(list_board)
    assert not(my_board.is_full())

def test_make_move():
    list_board = [['-', '-', '-'],
                  ['-', 'x', '-'],
                  ['x', '-', '-']]
    my_board = board()
    my_board.set_board(list_board)
    assert not(my_board.make_move(-1, -1, 'x'))
    assert my_board.make_move(0, 2, 'x')
    assert my_board.get_board() == [['-', '-', 'x'],
                                    ['-', 'x', '-'],
                                    ['x', '-', '-']]

def test_random_move():
    my_board = board()
    my_board.random_move('x')
    assert my_board.num_empty_cells() == 8

def test_winning_move():
    list_board = [['-', '-', '-'],
                  ['-', 'x', '-'],
                  ['x', '-', '-']]
    my_board = board()
    my_board.set_board(list_board)
    my_board.make_move(0, 2,'x')
    assert my_board.winning_move(0, 2)

def test_can_win():
    list_board = [['-', '-', '-'],
                  ['-', 'x', '-'],
                  ['x', '-', '-']]
    my_board = board()
    my_board.set_board(list_board)
    assert my_board.can_win('x')
    assert my_board.can_win('x') == (0, 2)

def test_make_pair():
    list_board = [['-', '-', '-'],
                  ['-', 'x', '-'],
                  ['-', '-', '-']]
    my_board = board()
    my_board.set_board(list_board)
    assert my_board.make_pair('x')
    assert my_board.make_pair('x') == (1, 0)
