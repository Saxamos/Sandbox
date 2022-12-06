puzzle = open("3.txt").read().split("\n")

# 1
import string

sol_1 = 0
for sac in puzzle:
    mid = len(sac) // 2
    c1 = sac[:mid]
    c2 = sac[mid:]
    for char in c1:
        if char in c2:
            if char.isupper():
                sol_1 += 26
                char = char.lower()
            sol_1 += string.ascii_lowercase.index(char) + 1
            break

# 2
sol_2 = 0
for i in range(0, len(puzzle), 3):
    char = (
        set(puzzle[i]).intersection(set(puzzle[i + 1])).intersection(set(puzzle[i + 2]))
    )
    char = list(char)[0]
    if char.isupper():
        sol_2 += 26
        char = char.lower()
    sol_2 += string.ascii_lowercase.index(char) + 1

print("solutions:", sol_1, sol_2)
