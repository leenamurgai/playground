from diff import func
from diff import diff

def test_func():
    assert func(3) == 4

def test_diff():
    dict1 = {'a':1, 'b':2}
    dict2 = {'c':2, 'd':3}
    assert diff(dict1, dict2) == ('a', 'c'), 'diff test 1 failed'
