puzzle = open("7.txt").read().split("\n")

# 1
solution_1 = set()


def filter_color(s: str) -> str:
    return s[2:].split(" bag")[0]


color_dag = {}
for el in puzzle:
    if "bags contain no other bags" in el:
        continue
    else:
        first_color, contained_colors = el.split(" bags contain ")
        color_dag[first_color] = {filter_color(color): int(color[0]) for color in contained_colors.split(", ")}


def recursively_find_colors(color: str, solution: set) -> None:
    for k, v in color_dag.items():
        if color in v.keys():
            solution |= {k}
            recursively_find_colors(k, solution)


recursively_find_colors("shiny gold", solution_1)

# 2
solution_2 = 0


def recursively_find_bags_number(color: str, mult: int) -> None:
    global solution_2
    if color in color_dag:
        for col, number in color_dag[color].items():
            solution_2 += number * mult
            recursively_find_bags_number(col, number * mult)


recursively_find_bags_number("shiny gold", 1)

print("solutions:", len(solution_1), solution_2)
