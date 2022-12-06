entries = list(map(str, open("2.txt").read().split("\n")))

# 1
sol_1 = 0
for el in entries:
    a, b = el.split(" ")
    if b == "X":  # rock
        sol_1 += 1
        if a == "A":
            sol_1 += 3
        elif a == "C":
            sol_1 += 6

    elif b == "Y":  # paper
        sol_1 += 2
        if a == "A":
            sol_1 += 6
        elif a == "B":
            sol_1 += 3

    else:  # scissors
        sol_1 += 3
        if a == "B":
            sol_1 += 6
        elif a == "C":
            sol_1 += 3

# 2
sol_2 = 0
for el in entries:
    a, b = el.split(" ")
    if b == "X":  # loose
        if a == "A":
            sol_2 += 3
        elif a == "B":
            sol_2 += 1
        elif a == "C":
            sol_2 += 2

    elif b == "Y":  # draw
        sol_2 += 3
        # use the same item for a draw
        if a == "A":
            sol_2 += 1
        elif a == "B":
            sol_2 += 2
        else:
            sol_2 += 3

    else:  # win
        sol_2 += 6
        if a == "A":
            sol_2 += 2
        elif a == "B":
            sol_2 += 3
        elif a == "C":
            sol_2 += 1

print("solutions:", sol_1, sol_2)
