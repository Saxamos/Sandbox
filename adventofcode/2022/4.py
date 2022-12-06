puzzle = open("4.txt").read().split("\n")

# 1
solution_1 = 0
for elve in puzzle:
    s1, s2 = elve.split(",")
    start_1, end_1 = [int(el) for el in s1.split("-")]
    start_2, end_2 = [int(el) for el in s2.split("-")]
    if (start_1 >= start_2 and end_1 <= end_2) or (
        start_1 <= start_2 and end_1 >= end_2
    ):
        solution_1 += 1


# 2
solution_2 = 0
for elve in puzzle:
    s1, s2 = elve.split(",")
    start_1, end_1 = [int(el) for el in s1.split("-")]
    start_2, end_2 = [int(el) for el in s2.split("-")]
    if end_1 < start_2 or start_1 > end_2:
        continue
    solution_2 += 1


print("solutions:", solution_1, solution_2)
