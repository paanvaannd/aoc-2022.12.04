#!/usr/bin/env python

# Import built-in libraries
from collections import namedtuple

Pair = namedtuple("Pair", "elf_one, elf_two")
Assignment = namedtuple("Assignment", "beginning, end")

with open("data.txt", "r") as file:
    data = file.read().splitlines()

complete_overlaps: int = 0
partial_overlaps: int = 0
line: int
for line in data:
    _pair: list
    assignments: list = [_pair.split("-") for _pair in line.split(sep=",")]
    pair = Pair(elf_one=Assignment(beginning=int(assignments[0][0]),
                                   end=int(assignments[0][1])),
                elf_two=Assignment(beginning=int(assignments[1][0]),
                                   end=int(assignments[1][1])))

    if ((pair.elf_one.beginning <= pair.elf_two.beginning and  # part 1
         pair.elf_one.end >= pair.elf_two.end) or 
        (pair.elf_two.beginning <= pair.elf_one.beginning and
         pair.elf_two.end >= pair.elf_one.end)):
        complete_overlaps += 1
    else:  # part 2
        if any(set(range(pair.elf_one.beginning, pair.elf_one.end + 1)) &
               set(range(pair.elf_two.beginning, pair.elf_two.end + 1))):
            partial_overlaps += 1

all_overlaps: int = partial_overlaps + complete_overlaps
print(f"{complete_overlaps} section assignments overlapped completely.\n"
      f"{all_overlaps} section assgnments overlapped to any degree.")
