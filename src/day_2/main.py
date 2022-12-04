import pandas as pd
from src.day_2.repo_scissors import You, Me, Issue


def load_strategy():
    df = pd.read_csv("src/day_2/input.txt", sep=' ', header=None)
    df.columns = ["you", "issue"]
    return df


def compute_scissors_score():
    strategies = load_strategy()
    strategies = strategies.assign(
        **{
            "me": lambda df: df.apply(lambda row: find_my_hand(row["you"], row["issue"]), axis=1),
            "score": lambda df: df.apply(lambda row: score_hand(row["you"], row["me"]), axis=1),
            })
    strategies["score"].sum()
    return 0


def find_my_hand(you: You, issue: Issue) -> Me:
    you = You(you)
    issue = Issue(issue)
    if you == You.SCISSORS:
        if issue == Issue.DRAW:
            me = Me.SCISSORS
        elif issue == Issue.LOOSE:
            me = Me.PAPER
        else:
            me = Me.ROCK
    elif you == You.ROCK:
        if issue == Issue.DRAW:
            me = Me.ROCK
        elif issue == Issue.LOOSE:
            me = Me.SCISSORS
        else:
            me = Me.PAPER
    elif you == You.PAPER:
        if issue == Issue.DRAW:
            me = Me.PAPER
        elif issue == Issue.LOOSE:
            me = Me.ROCK
        else:
            me = Me.SCISSORS
    return me

            
def score_hand(you: You, me: Me):
    you = You(you)
    me = Me(me)
    if me == Me.ROCK:
        hand = 1
        if you == You.SCISSORS:
            victory = 6
        if you == You.ROCK:
            victory = 3
        if you == You.PAPER:
            victory = 0
            
    if me == Me.PAPER:
        hand = 2
        if you == You.ROCK:
            victory = 6
        if you == You.PAPER:
            victory = 3
        if you == You.SCISSORS:
            victory = 0

    if me == Me.SCISSORS:
        hand = 3
        if you == You.PAPER:
            victory = 6
        if you == You.SCISSORS:
            victory = 3
        if you == You.ROCK:
            victory = 0
    return victory + hand