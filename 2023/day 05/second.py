from typing import Tuple, List
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
        self.mappings = sorted(mappings, key=lambda m: m.source)

    def map(self, ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        result_ranges: List[Tuple[int, int]] = []
        for r in ranges:
            result_ranges.extend(self.map_range(*r))

        return result_ranges

    def map_range(self, start, length) -> List[Tuple[int, int]]:
        ranges = []
        end = start + length  # non inclusive
        for mapping in self.mappings:
            if start < mapping.source:
                ranges.append((start, min(mapping.source - start, length)))
                start += mapping.source - start

            if start >= end - 1:
                break

            if start in mapping:
                r, start = mapping.map(start, end)
                ranges.append(r)

                if start >= end - 1:
                    break

        if start < end - 1:
            ranges.append((start, end - start))

        return ranges

    def __repr__(self):
        return "\n".join(
            str(x) for x in self.mappings
        )


class Mapping:
    def __init__(self, row: str):
        self.destination, self.source, self.range_length = [int(x) for x in row.split(" ")]
        self.diff = self.destination - self.source

    def map(self, start, end) -> Tuple[Tuple[int, int], int]:
        source_start_diff = start - self.source
        return_end = min(self.source + self.range_length, end)
        return (self.destination + source_start_diff, return_end - start), return_end

    def __contains__(self, number: int) -> bool:
        return self.source <= number < self.source + self.range_length

    def __repr__(self) -> str:
        return f"source: {self.source}, destination: {self.destination}, range_length: {self.range_length}"

seeds_ranges = [int(x) for x in lines[0].split(": ")[1].split(" ")]
seeds = []
for i in range(0, len(seeds_ranges), 2):
    seeds.append([(seeds_ranges[i], seeds_ranges[i+1])])

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
        smallest = min([x[0] for x in seed])
    else:
        smallest = min(smallest, *[x[0] for x in seed])

print(smallest)
