import pandas as pd


def detail_parts(part):
    begin, end = [int(str_) for str_ in part.split("-")]
    full_part = set(range(begin, end+1))
    return full_part


def is_fully_contained(part1, part2):
    full_part1 = detail_parts(part1)
    full_part2 = detail_parts(part2)
    is_contained = full_part1.issubset(full_part2) or full_part2.issubset(full_part1)
    return is_contained


def is_overlap(part1, part2):
    full_part1 = detail_parts(part1)
    full_part2 = detail_parts(part2)
    overlap = full_part1.intersection(full_part2)
    return len(overlap) > 0

def main():
    pairs = pd.read_csv("src/day_4/input.txt", header=None)
    pairs.columns = ["elf1_part", "elf2_part"]
    pairs = pairs.assign(
        **{
            "is_fully_contained": lambda df: df.apply(
                lambda row: is_fully_contained(row["elf1_part"], row["elf2_part"]),
                axis=1,
            ),
            "is_overlap": lambda df: df.apply(
                lambda row: is_overlap(row["elf1_part"], row["elf2_part"]),
                axis=1,
            )
        }
    )
    number_of_contained_pairs = pairs["is_fully_contained"].sum()
    number_of_overlap = pairs["is_overlap"].sum()
    print('number_of_contained_pairs : ', number_of_contained_pairs)
    print('number_of_overlap : ', number_of_overlap)


if __name__ == "__main__":
    main()
