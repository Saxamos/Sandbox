puzzle = list(map(int, open("10.txt").read().split("\n")))

# 1
solution_1 = 0
sorted_puzzle = sorted(puzzle)
i = 0
diff_1, diff_3 = 1, 1
while i < len(sorted_puzzle) - 1:
    if sorted_puzzle[i + 1] - sorted_puzzle[i] == 1:
        diff_1 += 1
    elif sorted_puzzle[i + 1] - sorted_puzzle[i] == 3:
        diff_3 += 1
    i += 1
solution_1 = diff_1 * diff_3

# 2
solution_2 = 1
grp_1 = 2
i = 0
while i < len(sorted_puzzle):
    if i == len(sorted_puzzle) - 1 or sorted_puzzle[i + 1] - sorted_puzzle[i] == 3:
        if grp_1 == 3:
            solution_2 *= 2
        elif grp_1 == 4:
            solution_2 *= 4
        elif grp_1 == 5:
            solution_2 *= 7
        elif grp_1 > 5:
            raise NotImplemented
        grp_1 = 1
    elif sorted_puzzle[i + 1] - sorted_puzzle[i] == 1:
        grp_1 += 1
    i += 1

print("solutions:", solution_1, solution_2)
