puzzle = open("2.txt").read().split("\n")

# 1
solution_1 = 0
for line in puzzle:
    num, char, code = line.split(" ")

    k = 0
    for c in code:
        if c == char[0]:
            k += 1

    low, up = list(map(int, num.split("-")))
    if low <= k <= up:
        solution_1 += 1

# 2
solution_2 = 0
for line in puzzle:
    num, char, code = line.split(" ")
    first, second = list(map(int, num.split("-")))
    if (code[first - 1] == char[0] or code[second - 1] == char[0]) and not (
        code[first - 1] == char[0] and code[second - 1] == char[0]
    ):
        solution_2 += 1

print("solutions:", solution_1, solution_2)
