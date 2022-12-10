import pytest
from src.day_8.main import find_visible_trees, best_spot_score


def test_find_visible_trees():
    """
    ooooo
    ooo.o
    o..oo
    o.o.o
    ooooo
    """
    trees = \
        [
            [3,0,3,7,3,],
            [2,5,5,1,2,],
            [6,5,3,3,2,],
            [3,3,5,4,9,],
            [3,5,3,9,0,],
        ]
    resu = find_visible_trees(trees)
    assert resu == 21


def test_best_spot_score():
    """
    ooooo
    ooo.o
    o..oo
    o.o.o
    ooooo
    """
    trees = \
        [
            [3,0,3,7,3,],
            [2,5,5,1,2,],
            [6,5,3,3,2,],
            [3,3,5,4,9,],
            [3,5,3,9,0,],
        ]
    resu = best_spot_score(trees)
    assert resu == 8
