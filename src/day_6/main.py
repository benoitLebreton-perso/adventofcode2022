import re


def find_packet(pat: str, chain: str) -> int:
    match = re.search(pat, chain)
    return match.end()


def generate_packet_regex(length: int) -> str:
    """
    Generate the regex depending on the length of the pattern
    Thanks to backref and negative lookahead.
    Example for 2-length pattern :
    (\w)(?!\1)
    For 3-length pattern :
    (\w)(?!\1)(\w)(?!\1|\2)
    And for 4-length pattern :
    (\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)

    And we add a last \w at the end because we want the next letter
    AFTER the n-letter pattern
    Parameters
    ----------
    length : int
        length of the pattern (4 or 14 in the code challenge)

    Returns
    -------
    str
        regex that will find the pattern + the next letter
    """
    regex = ""
    negative_group = []
    for i in range(1, length):
        negative_group.append(f"\{i}")
        negative_pat = "|".join(negative_group)
        pat = r"(\w)(?!{})".format(negative_pat)
        regex = regex + pat
    return regex + "\w"


def main():
    with open("src/day_6/input.txt", "r") as f:
        chain = f.read()
    # pattern = generate_packet_regex(4)
    pattern = generate_packet_regex(14)
    begin_pattern = find_packet(pattern, chain)
    print(begin_pattern)


if __name__ == "__main__":
    main()
