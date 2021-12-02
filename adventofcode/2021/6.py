puzzle = list(map(int, open("6.txt").read().split(",")))

# 1
fishes = puzzle.copy()
day = 0
while day < 80:
    babies = 0
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            babies += 1
        else:
            fishes[i] -= 1

    fishes += [8] * babies
    day += 1

solution_1 = len(fishes)

# 2
fishes_by_age = [0] * 9
for el in puzzle:
    fishes_by_age[el] += 1

day = 0
while day < 256:
    to_reproduce = fishes_by_age.pop(0)
    fishes_by_age[6] += to_reproduce
    fishes_by_age.append(to_reproduce)
    day += 1

solution_2 = sum(fishes_by_age)

print("solutions:", solution_1, solution_2)
