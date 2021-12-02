import numpy as np

puzzle = open("11.txt").read().split("\n")

# 1
grid = np.array([[int(r) for r in row] for row in puzzle])
neighbor = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
solution_1 = 0
for _ in range(100):
    grid += 1
    xs, ys = np.where(grid == 10)
    while len(xs) > 0:
        solution_1 += 1
        grid[xs[0], ys[0]] = 0
        for n in neighbor:
            if 10 > xs[0] + n[0] >= 0 and 10 > ys[0] + n[1] >= 0:
                if grid[xs[0] + n[0], ys[0] + n[1]] not in [0, 10]:
                    grid[xs[0] + n[0], ys[0] + n[1]] += 1
        xs, ys = np.where(grid == 10)


# 2
grid = np.array([[int(r) for r in row] for row in puzzle])
solution_2 = 0
while True:
    flash = 0
    grid += 1
    xs, ys = np.where(grid == 10)
    while len(xs) > 0:
        flash += 1
        grid[xs[0], ys[0]] = 0
        for n in neighbor:
            if 10 > xs[0] + n[0] >= 0 and 10 > ys[0] + n[1] >= 0:
                if grid[xs[0] + n[0], ys[0] + n[1]] not in [0, 10]:
                    grid[xs[0] + n[0], ys[0] + n[1]] += 1
        xs, ys = np.where(grid == 10)
    solution_2 += 1
    if flash == grid.shape[0]*grid.shape[1]:
        break


print("solutions:", solution_1, solution_2)
