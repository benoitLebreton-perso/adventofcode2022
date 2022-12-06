import re


def find_packet(pat, chain):
    match = re.search(pat, chain)
    return match.end() + 1


def generate_packet_regex(length):
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
