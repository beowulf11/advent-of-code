from math import pow
import sys
import re


def read(test: bool = False):
    lines = []
    with open("test1.txt" if test else "input.txt", "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append(line.split(" "))
    return lines


class Hand:
    def __init__(self, cards, value):
        self.cards = [c for c in cards]
        self.value = int(value)
        self.hand_type = self.get_type()

    def get_type(self):
        card_set = list(set(self.cards))
        card_groups = {
            c: self.cards.count(c) for c in card_set
        }
        pair_count = sum([1 for value in card_groups.values() if value == 2])

        if len(card_set) == 1:
            return 7
        elif len(card_set) == 2 and (card_groups[card_set[0]] == 4 or card_groups[card_set[1]] == 4):
            return 6
        elif len(card_set) == 2:
            return 5
        elif len(card_set) == 3 and (card_groups[card_set[0]] == 3 or card_groups[card_set[1]] == 3 or card_groups[card_set[2]] == 3):
            return 4
        elif pair_count == 2:
            return 3
        elif pair_count == 1:
            return 2
        else:
            return 1

    def compare_transfor(self, i):
        if self.cards[i].isdigit():
            return ord(self.cards[i])
        match self.cards[i]:
            case 'A':
                return 90
            case 'K':
                return 89
            case 'Q':
                return 88
            case 'J':
                return 87
            case 'T':
                return 86

    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for i in range(5):
            a = self.compare_transfor(i)
            b = other.compare_transfor(i)
            if a != b:
                return a < b
        return True


    def __repr__(self):
        return f"{''.join(self.cards)} {self.value} - {self.hand_type}"


lines = read(len(sys.argv[1:]))
hands = sorted([Hand(*l) for l in lines])
hand_value = 0
for i, h in enumerate(hands):
    hand_value += h.value * (i + 1)

print(hand_value)
