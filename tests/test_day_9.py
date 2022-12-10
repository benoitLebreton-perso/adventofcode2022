import pytest
from src.day_9.main import move_head, Head, Tail


def test_move_head():
    head_moves = \
    """R 4
    U 4
    L 3
    D 1
    R 4
    D 1
    L 5
    R 2"""
    h = Head()
    t = Tail()
    move_head(h, t, head_moves)
    expected_positions = set()
    expected_positions.add((0,0))
    expected_positions.add((0,1))
    expected_positions.add((0,2))
    expected_positions.add((0,3))
    expected_positions.add((1,4))
    expected_positions.add((2,4))
    expected_positions.add((2,3))
    expected_positions.add((2,3))
    expected_positions.add((2,1))
    expected_positions.add((3,3))
    expected_positions.add((3,4))
    expected_positions.add((4,2))
    expected_positions.add((4,3))
    assert t.hist == expected_positions