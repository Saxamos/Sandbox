from functools import reduce

puzzle = open("6.txt").read().split("\n\n")

# 1
solution_1 = 0
for el in puzzle:
    answers = el.split("\n")
    answers = [set(el) for el in answers]
    solution_1 += len(reduce(lambda x, y: x | y, answers))

# 2
solution_2 = 0
for el in puzzle:
    answers = el.split("\n")
    answers = [set(el) for el in answers]
    solution_2 += len(reduce(lambda x, y: x & y, answers))

print("solutions:", solution_1, solution_2)
