puzzle = open("5.txt").read().split("\n")

# 1
solution_1 = 0
for seat in puzzle:
    row = seat[:7].replace('F', '0').replace('B', '1')
    col = seat[7:].replace('L', '0').replace('R', '1')
    n = int(row, 2) * 8 + int(col, 2)
    if n > solution_1:
        solution_1 = n

# 2
solution_2 = 0
ids = []
for seat in puzzle:
    row = seat[:7].replace('F', '0').replace('B', '1')
    col = seat[7:].replace('L', '0').replace('R', '1')
    ids.append(int(row, 2) * 8 + int(col, 2))

ids = sorted(ids)
i = 0
while i < len(ids):
    if ids[i + 1] != ids[i] + 1:
        solution_2 = ids[i] + 1
        break
    i += 1

print("solutions:", solution_1, solution_2)
