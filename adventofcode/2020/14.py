import itertools

puzzle = open("14.txt").read().split("\n")


# 1
memory = {}
for line in puzzle:
    splitted_line = line.split(" = ")
    if line.startswith("mask"):
        mask = splitted_line[1]
    else:
        bin_value = bin(int(splitted_line[1]))[2:]
        while len(bin_value) < len(mask):
            bin_value = "0" + bin_value
        bin_result = ""
        for m, b in zip(reversed(mask), reversed(bin_value)):
            if m != "X":
                bin_result = m + bin_result
            else:
                bin_result = b + bin_result
        memory[splitted_line[0][4:-1]] = int(bin_result, 2)
solution_1 = sum(memory.values())


# 2
def _find_indexes(s, ch):
    return [i for i, c in enumerate(s) if c == ch]


memory = {}
for line in puzzle:
    splitted_line = line.split(" = ")
    if line.startswith("mask"):
        mask = splitted_line[1]
    else:
        mem_value = int(splitted_line[1])

        bin_address = bin(int(splitted_line[0][4:-1]))[2:]
        while len(bin_address) < len(mask):
            bin_address = "0" + bin_address
        bin_add_result = ""
        for m, b in zip(reversed(mask), reversed(bin_address)):
            if m == "0":
                bin_add_result = b + bin_add_result
            else:
                bin_add_result = m + bin_add_result

        for el in list(itertools.product([0, 1], repeat=bin_add_result.count("X"))):
            address = list(bin_add_result)
            indexes = _find_indexes(address, "X")
            for i, b in zip(indexes, el):
                address[i] = str(b)
            memory[int("".join(address), 2)] = mem_value

solution_2 = sum(memory.values())

print("solutions:", solution_1, solution_2)
