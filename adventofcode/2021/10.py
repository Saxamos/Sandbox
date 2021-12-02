from statistics import median

puzzle = open("10.txt").read().split("\n")

# 1
solution_1 = 0
four_char_dict = {"(": 3, "[": 57, "{": 1197, "<": 25137}
four_char = list(four_char_dict.keys())
close_dict = {")": 1, "]": 2, "}": 3, ">": 4}
close = list(close_dict.keys())
correct = []
for index, line in enumerate(puzzle):
    i = 0
    pile = []
    while i < len(line):
        if line[i] in four_char:
            pile += line[i]
        else:
            for j, el in enumerate(close):
                if line[i] == el:
                    if pile[-1] == four_char[j]:
                        pile.pop(-1)
                    else:
                        expected = four_char[j]
                        found = pile[-1]
                        i = len(line)
                        solution_1 += four_char_dict[four_char[j]]
                        break
        i += 1
        if i == len(line):
            correct += [pile]

# 2
solution_2 = []
for el in correct:
    score = 0
    for c in reversed(el):
        score = score * 5 + close_dict[close[four_char.index(c)]]
    solution_2 += [score]

print("solutions:", solution_1, median(solution_2))
