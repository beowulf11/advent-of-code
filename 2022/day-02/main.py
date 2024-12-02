from enum import Enum


class Plays(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


# paper > rock     | 1 x - 2
# rock > scissors  | 0 x - 3
# scissors > paper | 2 x - 4
# paper win | 

def to_plays(value):
    if value == "A" or value == "X":
        return Plays.ROCK
    elif value == "B" or value == "Y":
        return Plays.PAPER
    elif value == "C" or value == "Z":
        return Plays.SCISSORS


def to_outcome(value):
    if value == "X":
        return "loss"
    elif value == "Y":
        return "tie"
    else:
        return "win"


def play_from_outcome(opponent, outcome):
    if outcome == "tie":
        return opponent
    elif outcome == "win":
        return Plays((opponent.value + 1) % 3)
    else:
        return Plays((opponent.value - 1) % 3)


def outcome_score(outcome):
    score = 0
    if outcome == "tie":
        score = 3
    elif outcome == "win":
        score = 6

    return score


def play_outcome(opponent, me):
    if me == opponent:
        return "tie"
    if (opponent.value + me.value) % 2 == 0:
        if me.value > opponent.value:
            return "win"
        else:
            return "loss"
    else:
        if me.value > opponent.value:
            return "loss"
        else:
            return "win"


def play_score(outcome, play):
    return outcome_score(outcome) + play.value + 1


def load():
    with open("input-1.txt") as f:
        return map(lambda x: x[:-1].split(" "), f.readlines())


# Part 1
plays = map(lambda x: (to_plays(x[0]), to_plays(x[1])), load())
print(sum(map(lambda p: play_score(play_outcome(p[1], p[0]), p[1]), plays)))

# Part 2
steps = map(lambda x: (to_plays(x[0]), to_outcome(x[1])), load())
print(sum(map(lambda p: play_score(p[1], play_from_outcome(p[0], p[1])), steps)))
