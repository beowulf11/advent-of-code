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

class Mapper:
    def __init__(self, mappings):
        self.mappings = mappings

    def map(self, number: int) -> int:
        mapping = next(filter(lambda m: number in m, self.mappings), None)
        if mapping is None:
            return number
        else:
            return mapping.map(number)
    def __repr__(self):
        return "\n".join(
            str(x) for x in self.mappings
        )

class Mapping:
    def __init__(self, row: str):
        self.destination, self.source, self.range_length = [int(x) for x in row.split(" ")]
        self.diff = self.destination - self.source

    def map(self, number: int) -> int:
        return number + self.diff

    def __contains__(self, number: int) -> bool:
        return self.source <= number < self.source + self.range_length

    def __repr__(self) -> str:
        return f"source: {self.source}, destination: {self.destination}, range_length: {self.range_length}"

seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]

mappers = [] #List of Mapper
mappings = []
for line in lines[3:]:
    if ":" in line:
        continue

    if line == "":
        mappers.append(Mapper(mappings))
        mappings = []
    else:
        mappings.append(Mapping(line))
mappers.append(Mapper(mappings))

smallest = None
for seed in seeds:
    for mapper in mappers:
        seed = mapper.map(seed)

    if smallest is None:
        smallest = seed
    else:
        smallest = min(smallest, seed)

print(smallest)
