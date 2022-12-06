import re


def load_instructions(path_to_data):
    with open(path_to_data, "r") as i:
        full_text = i.read()
    begin_schema, instruction_lines = full_text.split("\n\n")
    instruction_list = instruction_lines.split("\n")
    return instruction_list


def parse(instruction):
    parsed = re.search(r"move (\d+) from (\d+) to (\d+)", instruction)
    str_parsed = parsed.groups()
    int_parsed = (int(num) for num in str_parsed)
    return int_parsed


def move_crate(crates_schema, instruction):
    quant, from_, to_ = parse(instruction)
    for i in range(quant):
        crate = crates_schema[from_ - 1].pop()
        crates_schema[to_ - 1].append(crate)


def move_crates_by_pack(crates_schema, instruction):
    quant, from_, to_ = parse(instruction)
    tops = crates_schema[from_ - 1][-quant:]
    crates_schema[to_ - 1].extend(tops)
    for i in range(quant):
        crate = crates_schema[from_ - 1].pop()


def read_top_only(crates_schema):
    top_list = [stack[-1] for stack in crates_schema]
    string_ = "".join(top_list)
    return string_


def init(path_to_data):
    stack_1 = ["F", "D", "B", "Z", "T", "J", "R", "N"]
    stack_2 = ["R", "S", "N", "J", "H"]
    stack_3 = ["C", "R", "N", "J", "G", "Z", "F", "Q"]
    stack_4 = ["F", "V", "N", "G", "R", "T", "Q"]
    stack_5 = ["L", "T", "Q", "F"]
    stack_6 = ["Q", "C", "W", "Z", "B", "R", "G", "N"]
    stack_7 = ["F", "C", "L", "S", "N", "H", "M"]
    stack_8 = ["D", "N", "Q", "M", "T", "J"]
    stack_9 = ["P", "G", "S"]
    begin_crates_schema = (
        stack_1,
        stack_2,
        stack_3,
        stack_4,
        stack_5,
        stack_6,
        stack_7,
        stack_8,
        stack_9,
    )
    instructions = load_instructions(path_to_data)
    return begin_crates_schema, instructions


def main(path_to_data):
    begin_crates_schema, instructions = init(path_to_data)
    for move in instructions:
        move_crate(begin_crates_schema, move)
    string_ = read_top_only(begin_crates_schema)


def main_by_pack(path_to_data):
    begin_crates_schema, instructions = init(path_to_data)
    for move in instructions:
        move_crates_by_pack(begin_crates_schema, move)
    string_ = read_top_only(begin_crates_schema)


if __name__ == "__main__":
    path_to_data = "src/day_5/input.txt"
    # main(path_to_data)
    main_by_pack(path_to_data)
