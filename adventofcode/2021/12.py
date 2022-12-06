from collections import defaultdict

puzzle = open("12.txt").read().split("\n")

# 1
solution_1 = 0
graph = defaultdict(list)
while len(puzzle) > 0:
    i = 0
    while i < len(puzzle):
        a, b = puzzle[i].split("-")
        if a == "start":
            graph["start"] += [b]
            puzzle.pop(i)
        elif b == "start":
            graph["start"] += [a]
            puzzle.pop(i)

print(graph, puzzle)

# 2
solution_2 = 0

print("solutions:", solution_1, solution_2)
