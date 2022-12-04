from enum import Enum


class Me(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"

    def __gt__(self, other):
        pass


class You(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

class Issue(Enum):
    LOOSE = "X"
    DRAW = "Y"
    WIN = "Z"