
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
        self.card_set = list(set(self.cards))
        self.card_groups = {c: self.cards.count(c) for c in self.card_set}
        self.pair_count = sum([1 for value in self.card_groups.values() if value == 2])
        self.j_count = self.cards.count("J")
        self.hand_type = self.get_type()

    def is_five_of_a_kind(self):
        return len(self.card_set) == 1 or len(self.card_set) == 2 and "J" in self.card_set

    def is_four_of_a_kind(self):
        if len(self.card_set) == 2 and (self.card_groups[self.card_set[0]] == 4 or self.card_groups[self.card_set[1]] == 4):
            return True
        if len(self.card_set) == 3 and "J" in self.card_set:
            if any(map(lambda x: x == 3, self.card_groups.values())):
                return True
            if any(map(lambda x: x == 2, self.card_groups.values())) and self.j_count == 2:
                return True
            if any(map(lambda x: x == 1, self.card_groups.values())) and self.j_count == 3:
                return True
        return False

    def is_full_house(self):
        return len(self.card_set) == 2 or (len(self.card_set) == 3 and "J" in self.card_set)

    def is_three_of_a_kind(self):
        if len(self.card_set) == 3 and any(map(lambda x: x == 3, self.card_groups.values())):
            return True
        if "J" in self.card_set and self.pair_count > 0:
            return True

        return False

    def is_two_pair(self):
        if self.pair_count == 2:
            return True
        if self.j_count == 2:
            return True
        if self.pair_count == 1 and self.j_count == 1:
            return True

        return False

    def is_one_pair(self):
        if self.pair_count == 1:
            return True
        if self.j_count == 1:
            return True

        return False

    def get_type(self):
        if self.is_five_of_a_kind():
            return 7
        if self.is_four_of_a_kind():
            return 6
        if self.is_full_house():
            return 5
        if self.is_three_of_a_kind():
            return 4
        if self.is_two_pair():
            return 3
        if self.is_one_pair():
            return 2

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
                return 0
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
        return f"{''.join(sorted(self.cards))}, PC: {self.pair_count}, JC: {self.j_count}, Type: {self.hand_type}"


lines = read(len(sys.argv[1:]))
hands = sorted([Hand(*l) for l in lines])
hand_value = 0
for i, h in enumerate(hands):
    hand_value += h.value * (i + 1)

print(hand_value)
