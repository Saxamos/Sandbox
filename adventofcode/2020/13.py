import numpy

puzzle = open("13.txt").read().split("\n")

# 1
bus_id = int(puzzle[0])
bus_departure = [int(d) for d in puzzle[1].split(",") if d != "x"]
wait = [d - bus_id % d for d in bus_departure]
solution_1 = min(wait) * bus_departure[numpy.argmin(wait)]

# 2
bus_departure = [int(d) for d in puzzle[1].replace("x", "0").split(",")]
solution_2 = bus_departure[0]
step = bus_departure[0]
for dep in bus_departure[1:]:
    if dep == 0:
        continue
    while True:
        if (solution_2 + bus_departure.index(dep)) % dep == 0:
            break
        solution_2 += step
    step = numpy.lcm(step, dep)

print("solutions:", solution_1, solution_2)
