import re


def find_packet(pat, chain):
    """
    we find the 4-char pattern and finally 
    the next char is the one we are looking for
    """
    match = re.search(pat, chain)
    return match.end() + 1


def generate_packet_regex(length):
    """
    Thanks to backref and negative lookahead
    Example for 2-length pattern : 
    (\w)(?!\1)
    For 3-length pattern : 
    (\w)(?!\1)(\w)(?!\1|\2)
    And for 4-length pattern : 
    (\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)

    """
    regex = ""
    negative_group = []
    for i in range(1, length):
        negative_group.append(f"\{i}")
        negative_pat = "|".join(negative_group)
        pat = r"(\w)(?!{})".format(negative_pat)
        regex = regex + pat
    return regex


def main():
    with open("src/day_6/input.txt", "r") as f:
        chain = f.read()
    pattern = generate_packet_regex(14)
    begin_pattern = find_packet(pattern, chain)
    print(begin_pattern)


if __name__ == "__main__":
    main()
