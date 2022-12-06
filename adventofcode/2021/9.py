import numpy as np

puzzle = open("9.txt").read().split("\n")

# 1
solution_1 = 0
grid = np.array([[int(r) for r in row] for row in puzzle])
row_len = grid.shape[0]
col_len = grid.shape[1]
low_coods = []
for i in range(row_len):
    for j in range(col_len):
        current = grid[i, j]
        neighbor = []
        if j > 0:
            neighbor.append(grid[i, j - 1])
        if j < col_len - 1:
            neighbor.append(grid[i, j + 1])
        if i > 0:
            neighbor.append(grid[i - 1, j])
        if i < row_len - 1:
            neighbor.append(grid[i + 1, j])

        if sum([1 for el in neighbor if current >= el]) == 0:
            low_coods += [(i, j)]
            solution_1 += current + 1


# 2
def propagate(low_cood, grid, memory):
    i, j = low_cood
    memory[i, j] = 1

    if i >= 1 and grid[i - 1, j] != 9 and memory[i - 1, j] != 1:
        memory = propagate((i - 1, j), grid, memory)

    if i < row_len - 1 and grid[i + 1, j] != 9 and memory[i + 1, j] != 1:
        memory = propagate((i + 1, j), grid, memory)

    if j >= 1 and grid[i, j - 1] != 9 and memory[i, j - 1] != 1:
        memory = propagate((i, j - 1), grid, memory)

    if j < col_len - 1 and grid[i, j + 1] != 9 and memory[i, j + 1] != 1:
        memory = propagate((i, j + 1), grid, memory)

    return memory


candidate = []
for low_cood in low_coods:
    memory = propagate(low_cood, grid, np.zeros(grid.shape))
    candidate.append(memory.sum())

solution_2 = np.prod(sorted(candidate)[-3:])

print("solutions:", solution_1, solution_2)
