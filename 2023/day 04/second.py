from math import pow
from functools import reduce
import sys
import re


def read(test: bool = False):
    lines = []
    with open("test1.txt" if test else "input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append(line)
    return lines


lines = read(len(sys.argv[1:]))

card_values = {}
cards = {i + 1: 1 for i in range(len(lines))}

lines = map(lambda x: x.split("Card ")[1], lines)
for card in lines:
    number, line = card.split(": ")
    winning, mine = line.split(" | ")
    winning_set = set(filter(lambda x: x, winning.split(" ")))
    mine_set = set(filter(lambda x: x, mine.split(" ")))
    card_values[int(number)] = len(winning_set.intersection(mine_set))

for card in cards.keys():
    value = card_values[card]
    max_value = min(len(card_values), value + card)
    for i in range(card + 1, max_value + 1):
        cards[i] += cards[card]


print(reduce(lambda x, y: x + y, cards.values()))
