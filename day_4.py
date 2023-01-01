#!/usr/bin/env python

# Import built-in libraries
from collections import namedtuple

Pair = namedtuple("Pair", "first, second")
Assignment = namedtuple("Assignment", "beginning, end")

with open("data.txt", "r") as file:
    data = file.read().splitlines()

overlap_counter: int = 0
line: int
for line in range(len(data)):
    assignments: list = [_line.split("-") for _line in data[line].split(sep=",")]
    pair = Pair(assignments[0], assignments[1])
    first = Assignment(int(pair.first[0]), int(pair.first[1]))
    second = Assignment(int(pair.second[0]), int(pair.second[1]))

    if ((first.beginning <= second.beginning and
         first.end >= second.end) or 
        (second.beginning <= first.beginning and
         second.end >= first.end)):
        overlap_counter += 1

print(f"{overlap_counter} completely overlapping assignments detected.")
