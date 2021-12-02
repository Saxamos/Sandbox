import numpy as np

puzzle = open("4.txt").read().split("\n\n")

# 1
solution_1 = 0
draws = puzzle[0]
score_grids = np.zeros((len(puzzle[1:]), 5, 5), dtype=int)
given_grids = np.array([np.fromstring(grid, dtype=int, sep='\n').reshape((5, 5)) for grid in puzzle[1:]])
found = False
for draw in draws.split(","):
    score_grids[np.where(given_grids == int(draw))] = 1

    for i in range(len(score_grids)):
        score_grid = score_grids[i]

        is_row = np.where(score_grid.sum(1) == 5)[0]
        if len(is_row) > 0:
            solution_1 = given_grids[i][np.where(score_grid == 0)].sum() * int(draw)
            found = True
            break
        is_col = np.where(score_grid.sum(0) == 5)[0]
        if len(is_col) > 0:
            solution_1 = given_grids[i][np.where(score_grid == 0)].sum() * int(draw)
            found = True
            break
    if found:
        break
# 2
solution_2 = 0
score_grids = np.zeros((len(puzzle[1:]), 5, 5), dtype=int)
for draw in draws.split(","):
    score_grids[np.where(given_grids == int(draw))] = 1

    i = 0
    while len(score_grids) > 1 and i < len(score_grids):
        score_grid = score_grids[i]

        is_row = np.where(score_grid.sum(1) == 5)[0]

        if len(is_row) > 0:
            score_grids = np.delete(score_grids, i, axis=0)
            given_grids = np.delete(given_grids, i, axis=0)
            i -= 1

        is_col = np.where(score_grid.sum(0) == 5)[0]
        if len(is_col) > 0:
            score_grids = np.delete(score_grids, i, axis=0)
            given_grids = np.delete(given_grids, i, axis=0)
            i -= 1

        i += 1

    if len(score_grids) == 1:
        is_row = np.where(score_grids[0].sum(1) == 5)[0]
        if len(is_row) > 0:
            solution_2 = given_grids[0][np.where(score_grids[0] == 0)].sum() * int(draw)
            found = True
            break
        is_col = np.where(score_grids[0].sum(0) == 5)[0]
        if len(is_col) > 0:
            solution_2 = given_grids[i][np.where(score_grids[0] == 0)].sum() * int(draw)
            found = True
            break

print("solutions:", solution_1, solution_2)
