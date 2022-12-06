import numpy as np

puzzle = open("5.txt").read().split("\n")

# 1
grid = np.zeros((1000, 1000))
for line in puzzle:
    xy1, xy2 = line.split(" -> ")
    x1, y1 = list(map(int, xy1.split(",")))
    x2, y2 = list(map(int, xy2.split(",")))
    if x1 == x2:
        if y1 < y2:
            grid[x1, y1 : y2 + 1] += 1
        else:
            grid[x1, y2 : y1 + 1] += 1
    elif y1 == y2:
        if x1 < x2:
            grid[x1 : x2 + 1, y1] += 1
        else:
            grid[x2 : x1 + 1, y1] += 1

solution_1 = (grid > 1).sum()

# 2
grid = np.zeros((1000, 1000))
for line in puzzle:
    xy1, xy2 = line.split(" -> ")
    x1, y1 = list(map(int, xy1.split(",")))
    x2, y2 = list(map(int, xy2.split(",")))
    if x1 == x2:
        if y1 < y2:
            grid[x1, y1 : y2 + 1] += 1
        else:
            grid[x1, y2 : y1 + 1] += 1
    elif y1 == y2:
        if x1 < x2:
            grid[x1 : x2 + 1, y1] += 1
        else:
            grid[x2 : x1 + 1, y1] += 1
    else:

        while True:
            grid[x1, y1] += 1
            if x1 == x2:
                break
            if x1 < x2:
                x1 += 1
            else:
                x1 -= 1
            if y1 < y2:
                y1 += 1
            else:
                y1 -= 1

solution_2 = (grid > 1).sum()

print("solutions:", solution_1, solution_2)
