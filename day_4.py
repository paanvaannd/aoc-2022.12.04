#!/usr/bin/env python

with open("data.txt", "r") as file:
    data = file.read().splitlines()
with open("output.txt", "a") as output:
    pair_counter: int = 0  # What's the difference between this and "line"?
    overlap_counter: int = 0
    line: str
    for line in range(len(data)):
        overlaps_in_pair: int = 0
        pair_counter += 1

        pair_assignments: list = [_.split("-") for _ in data[line].split(sep=",")]
        assignment_1 = range(int(pair_assignments[0][0]),
                            int(pair_assignments[0][1]))
        assignment_2 = range(int(pair_assignments[1][0]),
                            int(pair_assignments[1][1]))

        if assignment_1.start == assignment_1.stop:
            assignment_1: int = assignment_1.start
        if assignment_2.start == assignment_2.stop:
            assignment_2: int = assignment_2.start

        if isinstance(assignment_1, range) and isinstance(assignment_2, range):
            if ((assignment_1.start in assignment_2 and
                assignment_1.stop in assignment_2) or
                (assignment_2.start in assignment_1 and
                assignment_2.stop in assignment_1) or
                (assignment_1.start == assignment_2.start and
                assignment_1.stop == assignment_2.stop) or
                (assignment_1.stop == assignment_2.stop)):
                overlap_counter += 1
                overlaps_in_pair += 1
            else:
                output.write(str(pair_counter) + ": " + data[line] + "\n")
        elif (isinstance(assignment_1, int) and isinstance(assignment_2, range)):
            if ((assignment_1 in assignment_2) or 
                (assignment_1 == assignment_2.stop)):
                overlap_counter += 1
                overlaps_in_pair += 1
            else:
                output.write(str(pair_counter) + ": " + data[line] + "\n")
        elif (isinstance(assignment_2, int) and isinstance(assignment_1, range)):
            if ((assignment_2 in assignment_1) or
                (assignment_2 == assignment_1.stop)):
                overlap_counter += 1
                overlaps_in_pair += 1
            else:
                output.write(str(pair_counter) + ": " + data[line] + "\n")
        elif (isinstance(assignment_1, int) and isinstance(assignment_2, int)):
            if assignment_1 == assignment_2:
                overlap_counter += 1
                overlaps_in_pair += 1
            else:
                output.write(str(pair_counter) + ": " + data[line] + "\n")

print(f"{overlap_counter} completely overlapping assignments detected.")
