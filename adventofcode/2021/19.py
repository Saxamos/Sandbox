from typing import List

rules, texts = open("19.txt").read().split("\n\n")

# 1
rules = rules.split("\n")
rules_list = [""] * 200
for el in rules:
    splitted_rule = el.split(": ")
    rules_list[int(splitted_rule[0])] = splitted_rule[1]


def recursively_append(rules_list: List[str], rule_index: str, valid_patterns: List[str]) -> List[str]:
    rule = rules_list[int(rule_index)]
    if "a" in rule:
        valid_patterns = [pat + "a" for pat in valid_patterns]
    elif "b" in rule:
        valid_patterns = [pat + "b" for pat in valid_patterns]
    else:
        or_splitted_rule = rule.split(" | ")
        if len(or_splitted_rule) == 2:
            valid_patterns_1 = valid_patterns.copy()
            for index in or_splitted_rule[0].split(" "):
                valid_patterns = recursively_append(rules_list, index, valid_patterns)
            for index in or_splitted_rule[1].split(" "):
                valid_patterns_1 = recursively_append(rules_list, index, valid_patterns_1)
            valid_patterns = valid_patterns + valid_patterns_1
        else:
            for index in rule.split(" "):
                valid_patterns = recursively_append(rules_list, int(index), valid_patterns)
    return valid_patterns


solution_1 = 0
texts = texts.split("\n")
# valid_patterns = recursively_append(rules_list, "0", [""])
# for text in texts:
#     if text in valid_patterns:
#         solution_1 += 1

# 2
solution_2 = 0
rules_list[8] = "42 | 42 8"
rules_list[11] = "42 31 | 42 11 31"

patterns_42 = recursively_append(rules_list, "42", [""])
patterns_31 = recursively_append(rules_list, "31", [""])
"""
42 42 31 | 42 42 11 31                           | 42 8 42 3                   | 42 8 42 11 31
42 42 31 | 42 42 42 31 31 | 42 42 42 11 31 31    | 42 42 42 31 | 42 42 8 42 31 | 42 42 42 11 31 | 42 42 8 42 11 31 | 
42 42 42 42 31 31 | 42 42 8 42 42 11 31 31 

42 42 31
42 42 42 31 31
42 42 42 31
42 42 42 42 31 31
"""
assert len(patterns_42) == len(patterns_31)
assert len(patterns_42[0]) == len(patterns_31[0])

for text in texts:
    chunk_size = len(patterns_42[0])
    if len(text) % chunk_size != 0:
        continue
    n_pattern = len(text) // chunk_size

    i = 1
    valid = False
    while (n_pattern - i) > i and not valid:
        valid = True
        pattern_array = [patterns_42] * (n_pattern - i) + [patterns_31] * i
        for pattern_index, valid_patterns in enumerate(pattern_array):
            if not text[pattern_index * chunk_size : (pattern_index + 1) * chunk_size] in valid_patterns:
                valid = False
                break
        if valid:
            solution_2 += 1
        i += 1

print("solutions:", solution_1, solution_2)
