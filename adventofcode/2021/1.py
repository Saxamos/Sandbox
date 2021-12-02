entries = list(map(int, open("1.txt").read().split("\n")))

# 1
i = 1
increase_count = 0

while i < len(entries):
    depth_diff = entries[i] - entries[i - 1]
    if depth_diff == 0:
        print("no diff for", i)
    elif depth_diff > 0:
        increase_count += 1
    i += 1

print("solution 1 is:", increase_count)

# 2
i = 3
increase_count = 0

while i < len(entries):
    diff_sum = entries[i] - entries[i - 3]
    if diff_sum > 0:
        increase_count += 1
    i += 1

print("solution 2 is:", increase_count)

