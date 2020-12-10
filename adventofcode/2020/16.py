import numpy

puzzle = open("16.txt").read().split("\n\n")

rules = puzzle[0].split("\n")
my_ticket = list(map(int, puzzle[1].split("\n")[1].split(",")))
tickets = puzzle[2].split("\n")[1:]
patterns = []
for rule in rules:
    pattern = rule.split(": ")[1].split(" or ")
    s_1, e_1 = pattern[0].split("-")
    s_2, e_2 = pattern[1].split("-")
    patterns += [(int(s_1), int(e_1), int(s_2), int(e_2))]

# 1
invalid_numbers = []
valid_tickets = []
for ticket in tickets:
    numbers = list(map(int, ticket.split(",")))
    is_ticket_valid = True
    for n in numbers:
        is_valid = False
        for p in patterns:
            s_1, e_1, s_2, e_2 = p
            if s_1 <= n <= e_1 or s_2 <= n <= e_2:
                is_valid = True
                break
        if not is_valid:
            is_ticket_valid = False
            invalid_numbers += [n]
            break
    if is_ticket_valid:
        valid_tickets += [ticket]

solution_1 = sum(invalid_numbers)

# 2
patterns_index_not_comp_with_col_indexes = [[] for _ in range(len(patterns))]
matrix = numpy.array([t.split(",") for t in valid_tickets], dtype=int)

for pattern_index, (s_1, e_1, s_2, e_2) in enumerate(patterns):
    for col_index in range(matrix.shape[1]):
        for el in matrix[:, col_index]:
            if not (s_1 <= el <= e_1 or s_2 <= el <= e_2):
                patterns_index_not_comp_with_col_indexes[pattern_index] += [col_index]
                break

p_size = [len(p) for p in patterns_index_not_comp_with_col_indexes]
mapping = {}
already_taken = set()
for i in reversed(range(len(patterns))):
    pattern_index = p_size.index(i)
    candidate = list((set(range(20)) - set(patterns_index_not_comp_with_col_indexes[pattern_index]) - already_taken))[0]
    mapping[pattern_index] = candidate
    already_taken.add(candidate)

solution_2 = 1
for i in range(6):
    solution_2 *= my_ticket[mapping[i]]

print("solutions:", solution_1, solution_2)
