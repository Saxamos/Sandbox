entries = list(map(int, open("1.txt").read().split("\n")))

# 1
i = 0
while True:
    cur_el = entries[i]
    val = 2020 - cur_el
    i += 1
    if val not in entries:
        continue
    for el in entries[i:]:
        if el == val:
            print(el * cur_el)
            break
    break

# 2
for i in range(len(entries)):
    el_1 = entries[i]
    for j in range(i, len(entries)):
        el_2 = entries[j]
        val = 2020 - (el_1 + el_2)
        if val not in entries:
            continue
        for el in entries[j:]:
            if el == val:
                print(el * el_1 * el_2)

print("solutions:", 964875, 158661360)
