from copy import deepcopy

puzzle = open("5.txt").read().split("\n")

# """init
#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# """
# stack_0 = [["N", "Z"], ["D", "C", "M"], ["P"]]
"""init
    [C]             [L]         [T]
    [V] [R] [M]     [T]         [B]
    [F] [G] [H] [Q] [Q]         [H]
    [W] [L] [P] [V] [M] [V]     [F]
    [P] [C] [W] [S] [Z] [B] [S] [P]
[G] [R] [M] [B] [F] [J] [S] [Z] [D]
[J] [L] [P] [F] [C] [H] [F] [J] [C]
[Z] [Q] [F] [L] [G] [W] [H] [F] [M]
 1   2   3   4   5   6   7   8   9 
"""
stack_0 = [
    ["G", "J", "Z"],
    ["C", "V", "F", "W", "P", "R", "L", "Q"],
    ["R", "G", "L", "C", "M", "P", "F"],
    ["M", "H", "P", "W", "B", "F", "L"],
    ["Q", "V", "S", "F", "C", "G"],
    ["L", "T", "Q", "M", "Z", "J", "H", "W"],
    ["V", "B", "S", "F", "H"],
    ["S", "Z", "J", "F"],
    ["T", "B", "H", "F", "P", "D", "C", "M"],
]

# 1
solution_1 = 0
stack = deepcopy(stack_0)
for line in puzzle:
    _, move, _, from_, _, to = line.split(" ")
    move, from_, to = int(move), int(from_) - 1, int(to) - 1
    for _ in range(move):
        stack[to] = [stack[from_].pop(0)] + stack[to]

solution_1 = "".join([s[0] for s in stack])

# 2
solution_2 = 0
stack = deepcopy(stack_0)
for line in puzzle:
    _, move, _, from_, _, to = line.split(" ")
    move, from_, to = int(move), int(from_) - 1, int(to) - 1
    stack[to] = stack[from_][:move] + stack[to]
    stack[from_] = stack[from_][move:]

solution_2 = "".join([s[0] for s in stack])

print("solutions:", solution_1, solution_2)
