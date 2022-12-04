import pytest
from src.day_1.main import compute_find_elve_whith_most_calories


def test_elves_who_has_the_most_calories():
    path_to_data = "tests/data_calories.txt"
    # path_to_data = "/Users/blebreton/adventofcode/day_1/input.txt"
    elve_with_the_most_of_calories = compute_find_elve_whith_most_calories(path_to_data)
    assert elve_with_the_most_of_calories == 24000
