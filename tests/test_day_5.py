import pytest
from src.day_5.main import main, move_crate, parse, read_top_only, move_crates_by_pack


def test_move_crate(moves, begin_crates_schema):
    """
    expected_output :
    [D]
    [N] [C]
    [Z] [M] [P]
    1   2   3
    """
    move_crate(begin_crates_schema, moves[0])
    assert begin_crates_schema == (["Z", "N", "D"], ["M", "C"], ["P"])
    string_ = read_top_only(begin_crates_schema)
    string_ == "DCP"


def test_move_crates(moves, begin_crates_schema):
    """
    expected_output :
            [D]
            [N]
            [Z]
    [M] [C] [P]
    1   2   3
    """
    for move in moves:
        move_crate(begin_crates_schema, move)
    assert begin_crates_schema == (["C"], ["M"], ["P", "D", "N", "Z"])
    string_ = read_top_only(begin_crates_schema)
    string_ == "CMZ"


def test_move_crates_by_pack(moves, begin_crates_schema):
    """
    expected_output :
            [D]
            [N]
            [Z]
    [M] [C] [P]
    1   2   3
    """
    for move in moves:
        move_crates_by_pack(begin_crates_schema, move)
    assert begin_crates_schema == (["M"], ["C"], ["P", "Z", "N", "D"])
    string_ = read_top_only(begin_crates_schema)
    string_ == "MCD"


def test_parse(moves):
    quant, from_, to_ = parse(moves[0])
    assert quant == 1
    assert from_ == 2
    assert to_ == 1

    quant, from_, to_ = parse(moves[1])
    assert quant == 3
    assert from_ == 1
    assert to_ == 3

    quant, from_, to_ = parse(moves[2])
    assert quant == 2
    assert from_ == 2
    assert to_ == 1

    quant, from_, to_ = parse(moves[3])
    assert quant == 1
    assert from_ == 1
    assert to_ == 2
