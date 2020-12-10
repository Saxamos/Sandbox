puzzle = open("3.txt").read().split("\n")


# 1
def tree(right, down):
    solution = 0
    row, col = 0, 0
    row_len = len(puzzle[0])

    while row + down < len(puzzle):
        row += down
        col += right
        col %= row_len
        if puzzle[row][col] == "#":
            solution += 1
    return solution


solution_1 = tree(3, 1)

# 2
solution_2 = tree(1, 1) * tree(3, 1) * tree(5, 1) * tree(7, 1) * tree(1, 2)

print("solutions:", solution_1, solution_2)
