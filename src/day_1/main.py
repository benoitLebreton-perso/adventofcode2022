import pandas as pd


def compute_find_elve_whith_most_calories(path_to_data):
    with open(path_to_data, 'r') as i:
        full_text = i.read()
    records_by_elves = full_text.split('\n\n')
    score_by_elf = {}
    for num_elf, elf in enumerate(records_by_elves):
        elf_calories = []
        records = elf.split("\n")
        for record in records:
            if record == '':
                record = "0"
            elf_calories.append(int(record))
        score_by_elf[num_elf] = sum(elf_calories)
    score_by_elf_pd = pd.DataFrame.from_dict(score_by_elf, 'index')
    # id_max = int(score_by_elf_pd.idxmax())
    # value_max = score_by_elf_pd[id_max]
    score_by_elf_pd.columns = ["col"]
    value_max = score_by_elf_pd.max()
    score_by_elf_3 = score_by_elf_pd.sort_values(by='col', ascending=False).iloc[:3]
    int(score_by_elf_3.sum())
    return int(value_max)