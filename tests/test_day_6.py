import pytest
from src.day_6.main import find_packet, generate_packet_regex


@pytest.mark.parametrize(
    "chain,length,expected_begin_pattern",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4, 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14, 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 14, 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 14, 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14, 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14, 26),
    ],
)
def test_find_packet(chain, length, expected_begin_pattern):
    """
    find the char after the first time {length} chars are uniques
    """
    pattern = generate_packet_regex(length)
    begin_pattern = find_packet(pattern, chain)
    assert begin_pattern == expected_begin_pattern
