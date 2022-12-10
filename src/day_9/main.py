import re
from enum import Enum


class Dir(Enum):
    UP = "U"
    LEFT = "L"
    DOWN = "D"
    RIGHT = "R"


class Point():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.hist = set()

    def move(self, dir: Dir, dist: int):
        for _ in range(dist):
            self.move_1(dir)

    def move_1(self, dir: Dir):
        match dir:
            case Dir.UP:
                self.y += 1
            case Dir.DOWN:
                self.y -= 1
            case Dir.LEFT:
                self.x -= 1
            case Dir.RIGHT:
                self.x += 1
        self.hist.add((self.x, self.y))

    def __repr__(self) -> str:
        return f"x={self.x},y={self.y}"


class Head(Point):
    def __init__(self) -> None:
        super().__init__()


class Tail(Point):

    def diag_align_y(self, head: Head):
        if self.y != head.y:
            self.y = head.y

    def diag_align_x(self, head: Head):
        if self.x != head.x:
            self.x = head.x

    def follow(self, head: Head):
        right_diff = head.x - self.x
        if right_diff > 1:
            self.move(Dir.RIGHT, right_diff-1)
            self.diag_align_y(head)
        left_diff = self.x - head.x
        if left_diff > 1:
            self.move(Dir.LEFT, left_diff-1)
            self.diag_align_y(head)
        up_diff = head.y - self.y
        if up_diff > 1:
            self.move(Dir.UP, up_diff-1)
            self.diag_align_x(head)
        down_diff = self.y - head.y
        if down_diff > 1:
            self.move(Dir.DOWN, down_diff-1)
            self.diag_align_x(head)
        

def main():
    with open("src/day_9/input.txt", "r") as f:
        head_moves = f.read()
    move_head(head_moves)


def parse_move(head_move: str):
    match = re.search(r"([ULDR]) (\d+)", head_move)
    dir, dist = match.groups()
    dist = int(dist)
    dir = Dir(dir)
    return dir, dist

def move_head(h: Head, t: Tail, head_moves: str):
    head_moves = head_moves.split("\n")
    for head_move in head_moves:
        dir, dist = parse_move(head_move)
        h.move(dir, dist)
        t.follow(h)

