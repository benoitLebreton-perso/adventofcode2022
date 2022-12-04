import pytest
from src.day_2.main import compute_scissors_score, score_hand, find_my_hand


def test_compute_scissors_score():
    score = compute_scissors_score()
    assert score == 0


@pytest.mark.parametrize(
    "you,me,score", 
    [
        ("A", "Y", 8),
        ("B", "X", 1),
        ("C", "Z", 6),
    ])
def test_score_hand(you, me, score):
    assert score_hand(you, me) == score


@pytest.mark.parametrize(
    "you,issue,score", 
    [
        ("A", "Y", 4),
        ("B", "X", 1),
        ("C", "Z", 7),
    ])
def test_full(you, issue, score):
    me = find_my_hand(you, issue)
    assert score_hand(you, me) == score