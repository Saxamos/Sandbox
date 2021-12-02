puzzle = open("3.txt").read().split("\n")

# 1
gamma_eps = [0] * len(puzzle[0])
for line in puzzle:
    for i in range(len(line)):
        gamma_eps[i] += int(line[i])
gamma = ""
for count in gamma_eps:
    if count > len(puzzle) / 2:
        gamma += "1"
    else:
        gamma += "0"
eps = gamma.replace("0", "x").replace("1", "0").replace("x", "1")

print("solution 1 is:", int(gamma, 2) * int(eps, 2))

# 2
kept_lines = puzzle.copy()
kept_lines2 = puzzle.copy()
ogr = 0
csr = 0
for i in range(len(puzzle[0])):

    if len(kept_lines) == 1:
        continue
    else:
        ones = 0
        for line in kept_lines:
            ones += int(line[i])
        if ones >= len(kept_lines) / 2:
            keep = "1"
        else:
            keep = "0"

        j = 0
        while j < len(kept_lines):
            if kept_lines[j][i] != keep:
                kept_lines.pop(j)
            else:
                j += 1

    if len(kept_lines2) == 1:
        continue
    else:
        ones = 0
        for line in kept_lines2:
            ones += int(line[i])
        if ones >= len(kept_lines2) / 2:
            keep = "0"
        else:
            keep = "1"

        j = 0
        while j < len(kept_lines2):
            if kept_lines2[j][i] != keep:
                kept_lines2.pop(j)
            else:
                j += 1

ogr = int(kept_lines[0], 2)
csr = int(kept_lines2[0], 2)

print("solution 2 is:", ogr * csr)
