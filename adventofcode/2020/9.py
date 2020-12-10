from typing import List

puzzle = list(map(int, open("9.txt").read().split("\n")))


# 1
def is_valid(number: int, list_25_previous: List[int]) -> bool:
    for el in list_25_previous:
        if number - el in list_25_previous and 2 * el != number:
            return True


solution_1 = 0
for i in range(25, len(puzzle)):
    list_25_previous = puzzle[i - 25:i]
    number = puzzle[i]
    if not is_valid(number, list_25_previous):
        solution_1 = number
        break

# 2
solution_2 = 0
start, end = 0, 1
while True:
    contiguous_sum = sum(puzzle[start:end + 1])
    if contiguous_sum == solution_1:
        solution_2 = min(puzzle[start:end + 1]) + max(puzzle[start:end + 1])
        break
    elif contiguous_sum < solution_1:
        end += 1
    elif contiguous_sum > solution_1:
        start += 1

print("solutions:", solution_1, solution_2)
