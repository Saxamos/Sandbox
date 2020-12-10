from copy import deepcopy
from typing import List

puzzle = open("11.txt").read().split("\n")
puzzle = [list(row) for row in puzzle]
AROUND = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

# 1
solution_1 = 0


def update_rule_1(seat_map: List[List[str]]) -> List[List[str]]:
    updated_map = deepcopy(seat_map)

    for row in range(len(seat_map)):
        for col in range(len(seat_map[0])):
            n_occupied = 0
            for r, c in AROUND:
                try:
                    if row + r >= 0 and col + c >= 0 and seat_map[row + r][col + c] == "#":
                        n_occupied += 1
                except IndexError:
                    pass

            if seat_map[row][col] == "L" and n_occupied == 0:
                updated_map[row][col] = "#"
            elif seat_map[row][col] == "#" and n_occupied >= 4:
                updated_map[row][col] = "L"
    return updated_map


updated_seats = deepcopy(puzzle)
tmp = update_rule_1(updated_seats)
while True:
    if tmp == updated_seats:
        break
    updated_seats = deepcopy(tmp)
    tmp = update_rule_1(tmp)

for row in tmp:
    for char in row:
        if char == "#":
            solution_1 += 1

# 2
solution_2 = 0


def update_rule_2(seat_map: List[List[str]]) -> List[List[str]]:
    updated_map = deepcopy(seat_map)

    for row in range(len(seat_map)):
        for col in range(len(seat_map[0])):
            n_occupied = 0
            for r, c in AROUND:

                try:
                    tmp_row, tmp_col = row + r, col + c
                    while True:
                        if not (tmp_row >= 0 and tmp_col >= 0):
                            break
                        elif seat_map[tmp_row][tmp_col] == ".":
                            tmp_row += r
                            tmp_col += c
                        elif seat_map[tmp_row][tmp_col] == "#":
                            n_occupied += 1
                            break
                        elif seat_map[tmp_row][tmp_col] == "L":
                            break
                except IndexError:
                    pass

            if seat_map[row][col] == "L" and n_occupied == 0:
                updated_map[row][col] = "#"
            elif seat_map[row][col] == "#" and n_occupied >= 5:
                updated_map[row][col] = "L"
    return updated_map


updated_seats = deepcopy(puzzle)
tmp = update_rule_2(updated_seats)
while True:
    if tmp == updated_seats:
        break
    updated_seats = deepcopy(tmp)
    tmp = update_rule_2(tmp)

for row in tmp:
    for char in row:
        if char == "#":
            solution_2 += 1

print("solutions:", solution_1, solution_2)
