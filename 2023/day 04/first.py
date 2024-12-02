from math import pow
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
result = 0

lines = map(lambda x: x.split(": ")[1], lines)
for card in lines:
    winning, mine = card.split(" | ")
    winning_set = set(filter(lambda x: x, winning.split(" ")))
    mine_set = set(filter(lambda x: x, mine.split(" ")))
    inter_len = len(winning_set.intersection(mine_set))
    if inter_len > 0:
        result += pow(2, inter_len - 1)

print(int(result))
