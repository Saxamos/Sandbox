from typing import List

puzzle = open("12.txt").read().split("\n")

# 1
solution_1 = 0
position = [90, 0, 0]
dir_mapping = {0: "N", 90: "E", 180: "S", 270: "W"}


def _update_pos(direction: str, number: int, position: List[int]) -> List[int]:
    if direction == "N":
        position[2] += number
    if direction == "S":
        position[2] -= number
    if direction == "E":
        position[1] += number
    if direction == "W":
        position[1] -= number
    return position


for el in puzzle:
    direction = el[0]
    number = int(el[1:])
    position = _update_pos(direction, number, position)
    if direction == "L":
        position[0] = (position[0] - number) % 360
    if direction == "R":
        position[0] = (position[0] + number) % 360
    if direction == "F":
        position = _update_pos(dir_mapping[position[0]], number, position)

solution_1 = abs(position[1]) + abs(position[2])

# 2
solution_2 = 0
position = [0, 0]
waypoint = [10, 1]
for el in puzzle:
    direction = el[0]
    number = int(el[1:])
    if direction == "N":
        waypoint[1] += number
    elif direction == "S":
        waypoint[1] -= number
    elif direction == "E":
        waypoint[0] += number
    elif direction == "W":
        waypoint[0] -= number
    elif direction in ["L", "R"]:
        if el in ["L90", "R270"]:
            new_x = -waypoint[1]
            new_y = waypoint[0]
        elif el in ["R90", "L270"]:
            new_x = waypoint[1]
            new_y = -waypoint[0]
        else:
            new_x = -waypoint[0]
            new_y = -waypoint[1]
        waypoint = [new_x, new_y]
    elif direction == "F":
        position[0] += waypoint[0] * number
        position[1] += waypoint[1] * number

solution_2 = abs(position[0]) + abs(position[1])

print("solutions:", solution_1, solution_2)
