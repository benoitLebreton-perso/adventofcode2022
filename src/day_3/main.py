import pandas as pd
import math


def cut_rucksack(rucksack):
    length = len(rucksack)
    cut = int(length / 2)
    half_1 = rucksack[:cut]
    half_2 = rucksack[cut:]
    return half_1, half_2


def find_common_element(half_1, half_2):
    common_element = set(half_1).intersection(half_2)
    return common_element.pop()


def priority(element):
    if element.islower():
        result = ord(element) - 96
    else:
        result = ord(element.lower()) - 70
    return result


def find_common_in_three(rucksack_list):
    ruck_1, ruck_2, ruck_3 = tuple(rucksack_list)
    common = set(ruck_1).intersection(ruck_2).intersection(ruck_3)
    return common.pop()


def main():
    ruckstacks_pd = pd.read_csv("day_3/input.txt", header=None)
    ruckstacks_pd.columns = ["ruckstack"]
    ruckstacks_pd[["half_1", "half_2"]] = (
        ruckstacks_pd["ruckstack"].apply(cut_rucksack).apply(pd.Series)
    )

    ruckstacks_pd = ruckstacks_pd.assign(
        **{
            "common_element": lambda df: df.apply(
                lambda row: find_common_element(row["half_1"], row["half_2"]), axis=1
            ),
            "priority": lambda df: df["common_element"].apply(priority),
        }
    )

    return ruckstacks_pd["priority"].sum()


def main_2():
    ruckstacks_pd = pd.read_csv("day_3/input.txt", header=None)
    ruckstacks_pd.columns = ["ruckstack"]
    ruckstacks_pd = ruckstacks_pd.reset_index()
    ruckstacks_pd = ruckstacks_pd.assign(
        **{
            "group": lambda df: df["index"].apply(lambda i: i % 3),
            "new_index": lambda df: df["index"].apply(lambda i: math.floor(i / 3)),
        }
    )
    ruckstacks_pivot = ruckstacks_pd.drop(columns=["index"]).pivot(
        index="new_index", columns="group", values="ruckstack"
    )
    ruckstacks_pivot.columns = ['part_1', 'part_2', 'part_3']
    ruckstacks_pivot = ruckstacks_pivot.assign(
        **{
            "common_element": lambda df: df.apply(
                lambda row: find_common_in_three([row["part_1"], row["part_2"], row["part_3"]]), axis=1
            ),
            "priority": lambda df: df["common_element"].apply(priority),
        }
    )

    return ruckstacks_pivot["priority"].sum()


if __name__ == "__main__":
    main_2()
