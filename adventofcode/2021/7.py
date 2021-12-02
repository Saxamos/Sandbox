import numpy as np
puzzle = list(map(int, open("7.txt").read().split(",")))

# 1
med = np.median(puzzle)
solution_1 = np.sum([np.abs(med - el) for el in puzzle])

# 2
align = int(np.mean(puzzle))
solution_2 = np.sum([sum(range(abs(el - align) + 1)) for el in puzzle])

print("solutions:", solution_1, solution_2)
