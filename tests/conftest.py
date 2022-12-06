import pytest

# from queue import SimpleQueue


@pytest.fixture()
def begin_crates_schema():
    """
    output :
        [D]
    [N] [C]
    [Z] [M] [P]
    1   2   3
    """

    stack_1 = []
    stack_1.append("Z")
    stack_1.append("N")

    stack_2 = []
    stack_2.append("M")
    stack_2.append("C")
    stack_2.append("D")

    stack_3 = []
    stack_3.append("P")
    return stack_1, stack_2, stack_3


@pytest.fixture()
def moves():
    moves_ = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    return moves_
