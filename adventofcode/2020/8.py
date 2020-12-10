from typing import List, Tuple

puzzle = open("8.txt").read().split("\n")


# 1
def look_over_instruction(input_puzzle: List) -> Tuple[int, List[int]]:
    solution = 0
    i, visited = 0, [0] * len(input_puzzle)
    while i < len(visited) and visited[i] < 1:
        instruction, number = input_puzzle[i][:3], int(input_puzzle[i][4:])
        visited[i] = 1
        if instruction == "acc":
            solution += number
            i += 1
        elif instruction == "jmp":
            i += number
        elif instruction == "nop":
            i += 1
    return solution, visited


solution_1, visited_1 = look_over_instruction(puzzle)

# 2
solution_2 = 0
visited_2 = [0] * len(puzzle)

for i in range(len(puzzle)):
    if visited_1[i] == 0:
        continue
    elif puzzle[i][:3] == "jmp":
        updated_puzzle = puzzle.copy()
        updated_puzzle[i] = updated_puzzle[i].replace("jmp", "nop")
        solution_2, visited_2 = look_over_instruction(updated_puzzle)
    elif puzzle[i][:3] == "nop":
        updated_puzzle = puzzle.copy()
        updated_puzzle[i] = updated_puzzle[i].replace("nop", "jmp")
        solution_2, visited_2 = look_over_instruction(updated_puzzle)
    if visited_2[-1]:
        break

print("solutions:", solution_1, solution_2)
