puzzle = open("2.txt").read().split("\n")

# 1
pos, depth = 0, 0

for line in puzzle:
    key, value = line.split(" ")

    if key == "forward":
        pos += int(value)
    elif key == "down":
        depth += int(value)
    else:
        depth -= int(value)

print("solution 1 is:", pos * depth)

# 2
pos, depth, aim = 0, 0, 0

for line in puzzle:
    key, value = line.split(" ")

    if key == "forward":
        pos += int(value)
        depth += int(value) * aim
    elif key == "down":
        aim += int(value)
    else:
        aim -= int(value)

print("solution 2 is:", pos * depth)
