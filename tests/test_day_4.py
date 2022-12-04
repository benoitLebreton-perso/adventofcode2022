import pytest
from src.day_4.main import is_fully_contained, is_overlap


@pytest.mark.parametrize(
    "part1,part2,expected_iscontained",
    [
        ("2-4", "6-8", False),
        ("2-3", "4-5", False),
        ("5-7", "7-9", False),
        ("2-8", "3-7", True),
        ("6-6", "4-6", True),
        ("2-6", "4-8", False),
        ("57-75", "76-76", False),
    ],
)
def test_is_fully_contained(part1, part2, expected_iscontained):
    is_contained = is_fully_contained(part1, part2)
    assert is_contained == expected_iscontained


@pytest.mark.parametrize(
    "part1,part2,expected_isoverlap",
    [
        ("2-4", "6-8", False),
        ("2-3", "4-5", False),
        ("5-7", "7-9", True),
        ("2-8", "3-7", True),
        ("6-6", "4-6", True),
        ("2-6", "4-8", True),
        ("57-75", "76-76", False),
    ],
)
def test_is_overlap(part1, part2, expected_isoverlap):
    is_overlap_ = is_overlap(part1, part2)
    assert is_overlap_ == expected_isoverlap
