from typing import List

puzzle = open("18.txt").read().split("\n")


# 1
def _compute(eq_without_parenthesis: List[str]) -> int:
    value = int(eq_without_parenthesis[0])
    for i in range(1, len(eq_without_parenthesis), 2):
        if eq_without_parenthesis[i] == "+":
            value += int(eq_without_parenthesis[i + 1])
        elif eq_without_parenthesis[i] == "*":
            value *= int(eq_without_parenthesis[i + 1])
    return value


def _find_end_parenthesis_and_replace(line: List[str], i: int) -> int:
    start_index = i
    while line[i] != ")":
        i += 1
        if line[i] == "(":
            line = _find_end_parenthesis_and_replace(line, i)
    end_index = i + 1
    inside_parenthesis = _compute(line[start_index + 1: end_index - 1])
    return line[:start_index] + [str(inside_parenthesis)] + line[end_index:]


solution_1 = 0
for line in puzzle:
    line = list(line.replace(" ", ""))
    while "(" in line:
        i = 0
        while True:
            if line[i] == "(":
                line = _find_end_parenthesis_and_replace(line, i)
                break
            i += 1
    solution_1 += _compute(line)


# 2
def _compute_add(eq_without_parenthesis: List[str]) -> List[str]:
    for i in range(1, len(eq_without_parenthesis), 2):
        if eq_without_parenthesis[i] == "+":
            v = [str(int(eq_without_parenthesis[i - 1]) + int(eq_without_parenthesis[i + 1]))]
            if i == 1:
                eq_without_parenthesis = v + eq_without_parenthesis[i + 2:]
            elif i == len(eq_without_parenthesis) - 1:
                eq_without_parenthesis = eq_without_parenthesis[:i - 2] + v
            else:
                eq_without_parenthesis = eq_without_parenthesis[:i - 1] + v + eq_without_parenthesis[i + 2:]
            return eq_without_parenthesis


def _compute_addition_first(eq_without_parenthesis: List[str]) -> int:
    while "+" in eq_without_parenthesis:
        eq_without_parenthesis = _compute_add(eq_without_parenthesis)
    value = int(eq_without_parenthesis[0])
    for i in range(1, len(eq_without_parenthesis), 2):
        value *= int(eq_without_parenthesis[i + 1])
    return value


def _find_end_parenthesis_and_replace(line: List[str], i: int) -> int:
    start_index = i
    while line[i] != ")":
        i += 1
        if line[i] == "(":
            line = _find_end_parenthesis_and_replace(line, i)
    end_index = i + 1
    inside_parenthesis = _compute_addition_first(line[start_index + 1: end_index - 1])
    return line[:start_index] + [str(inside_parenthesis)] + line[end_index:]


solution_2 = 0
for line in puzzle:
    line = list(line.replace(" ", ""))
    while "(" in line:
        i = 0
        while True:
            if line[i] == "(":
                line = _find_end_parenthesis_and_replace(line, i)
                break
            i += 1
    solution_2 += _compute_addition_first(line)

print("solutions:", solution_1, solution_2)
