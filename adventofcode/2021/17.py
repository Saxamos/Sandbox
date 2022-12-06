import itertools

import numpy

puzzle = open("17.txt").read().split("\n")


# 1
def _detect_neighbors(grid: numpy.ndarray, x: int, y: int, z: int) -> int:
    detected_neighbors = 0
    for neighbor in NEIGHBORS:
        try:
            if grid[x + neighbor[0], y + neighbor[1], z + neighbor[2]] == 1:
                detected_neighbors += 1
        except:
            pass
    return detected_neighbors


def _update_grid(input_grid: numpy.ndarray) -> numpy.ndarray:
    updated_grid = numpy.zeros(input_grid.shape, dtype=int)
    len_x, len_y, len_z = input_grid.shape
    for x in range(len_x):
        for y in range(len_y):
            for z in range(len_z):
                detected_neighbors = _detect_neighbors(input_grid, x, y, z)
                if (input_grid[x, y, z] == 1 and detected_neighbors in [2, 3]) or (
                        input_grid[x, y, z] == 0 and detected_neighbors == 3
                ):
                    updated_grid[x, y, z] = 1
    return updated_grid


NEIGHBORS = list(itertools.product(*[[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
NEIGHBORS.remove((0, 0, 0))
n_round = 6
y_start = len(puzzle)
x_start = len(puzzle[0])
grid = numpy.zeros((x_start + n_round * 2, y_start + n_round * 2, 1 + n_round * 2), dtype=int)
center = [el // 2 for el in grid.shape]
# init grid
for y, row in enumerate(puzzle, start=-4):
    for x, val in enumerate(row, start=-4):
        if val == "#":
            grid[x + center[0], y + center[1], center[2]] = 1
# start iteration
for i in range(n_round):
    grid = _update_grid(grid)
solution_1 = grid.sum()


# 2
def _detect_neighbors(grid: numpy.ndarray, x: int, y: int, z: int, w: int) -> int:
    detected_neighbors = 0
    for neighbor in NEIGHBORS:
        try:
            if grid[x + neighbor[0], y + neighbor[1], z + neighbor[2], w + neighbor[3]] == 1:
                detected_neighbors += 1
        except:
            pass
    return detected_neighbors


def _update_grid(input_grid: numpy.ndarray) -> numpy.ndarray:
    updated_grid = numpy.zeros(input_grid.shape, dtype=int)
    len_x, len_y, len_z, len_w = input_grid.shape
    for x in range(len_x):
        for y in range(len_y):
            for z in range(len_z):
                for w in range(len_w):
                    detected_neighbors = _detect_neighbors(input_grid, x, y, z, w)
                    if (input_grid[x, y, z, w] == 1 and detected_neighbors in [2, 3]) or (
                            input_grid[x, y, z, w] == 0 and detected_neighbors == 3
                    ):
                        updated_grid[x, y, z, w] = 1
    return updated_grid


NEIGHBORS = list(itertools.product(*[[-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
NEIGHBORS.remove((0, 0, 0, 0))
grid = numpy.zeros((x_start + n_round * 2, y_start + n_round * 2, 1 + n_round * 2, 1 + n_round * 2), dtype=int)
center = [el // 2 for el in grid.shape]
# init grid
for y, row in enumerate(puzzle, start=-4):
    for x, val in enumerate(row, start=-4):
        if val == "#":
            grid[x + center[0], y + center[1], center[2], center[3]] = 1
# start iteration
for i in range(n_round):
    grid = _update_grid(grid)
solution_2 = grid.sum()

print("solutions:", solution_1, solution_2)
