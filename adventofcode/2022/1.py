entries = list(map(str, open("1.txt").read().split("\n")))

# 1
sol_1 = 0
food = 0
for el in entries:
    if el:
        food += int(el)
    else:
        if food > sol_1:
            sol_1 = food
        food = 0

# 2
top_3 = [0, 0, 0]
food = 0
for el in entries:
    if el:
        food += int(el)
    else:
        if food > min(top_3):
            top_3.append(food)
            top_3 = sorted(top_3[1:])
        food = 0

print("solutions:", sol_1, sum(top_3))
