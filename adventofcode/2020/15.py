from collections import defaultdict

puzzle = open("15.txt").read().split("\n")
puzzle = puzzle[0].split(",")

# 1
turn = 1
number_turn_apparition_list = defaultdict(list)
while turn < 2021:
    if turn <= len(puzzle):
        current_number = int(puzzle[turn - 1])
    else:
        if (
            previous_number not in number_turn_apparition_list.keys()
            or len(number_turn_apparition_list[previous_number]) == 1
        ):
            current_number = 0
        else:
            current_number = turn - 1 - number_turn_apparition_list[previous_number][-2]

    number_turn_apparition_list[current_number] += [turn]
    previous_number = current_number
    turn += 1

solution_1 = current_number

# 2
while turn < 30000001:
    if (
        previous_number not in number_turn_apparition_list.keys()
        or len(number_turn_apparition_list[previous_number]) == 1
    ):
        current_number = 0
    else:
        current_number = turn - 1 - number_turn_apparition_list[previous_number][-2]

    if len(number_turn_apparition_list[current_number]):
        number_turn_apparition_list[current_number] = [number_turn_apparition_list[current_number][-1], turn]
    else:
        number_turn_apparition_list[current_number] += [turn]

    previous_number = current_number
    if turn % 100000 == 0:
        print(turn)
    turn += 1

solution_2 = current_number

print("solutions:", solution_1, solution_2)
