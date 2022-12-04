import pytest
from src.day_3.main import cut_rucksack, find_common_element, priority, find_common_in_three


@pytest.mark.parametrize(
    "rucksack,expected_half_1,expected_half_2",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        ("PmmdzqPrVvPwwTWBwg", "PmmdzqPrV", "vPwwTWBwg"),
    ],
)
def test_cut_ruckstack(rucksack, expected_half_1, expected_half_2):
    half_1, half_2 = cut_rucksack(rucksack)
    assert half_1 == expected_half_1
    assert half_2 == expected_half_2


@pytest.mark.parametrize(
    "half_1,half_2,expected_common_letter",
    [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrV", "vPwwTWBwg", "P")
    ]
)
def test_find_common_element(half_1, half_2, expected_common_letter):
    common_element = find_common_element(half_1, half_2)
    assert common_element == expected_common_letter


@pytest.mark.parametrize(
    "element,expected_priority",
    [
        ("p", 16),
        ("L", 38),
        ("P", 42),
        ("v", 22),
        ("t", 20),
        ("s", 19),
    ]
)
def test_priority(element, expected_priority):
    element_priority = priority(element)
    assert element_priority == expected_priority



@pytest.mark.parametrize(
    "rucksack_list,expected_common_letter",
    [
        (["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg"], "r"),
        (["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"], "Z"),
    ]
)
def test_find_common_in_three(rucksack_list, expected_common_letter):
    common_letter = find_common_in_three(rucksack_list)
    assert common_letter == expected_common_letter


