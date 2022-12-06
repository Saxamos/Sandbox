import re

puzzle = open("4.txt").read().split("\n\n")

# 1
solution_1 = 0
REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
for passport in puzzle:
    pp = {
        field.split(":")[0]: field.split(":")[1] for field in re.split("\n| ", passport)
    }
    if not REQUIRED_FIELDS - set(pp.keys()):
        solution_1 += 1

# 2
solution_2 = 0
for passport in puzzle:
    pp = {
        field.split(":")[0]: field.split(":")[1] for field in re.split("\n| ", passport)
    }
    if REQUIRED_FIELDS - set(pp.keys()):
        continue
    try:
        if not 1920 <= int(pp["byr"]) <= 2002:
            continue
        if not 2010 <= int(pp["iyr"]) <= 2020:
            continue
        if not 2020 <= int(pp["eyr"]) <= 2030:
            continue
        if not (
            pp["hgt"][-2:] == "cm"
            and 150 <= int(pp["hgt"][:-2]) <= 193
            or pp["hgt"][-2:] == "in"
            and 59 <= int(pp["hgt"][:-2]) <= 76
        ):
            continue
        if not re.search(r"^#[a-f0-9]{6}$", pp["hcl"]):
            continue
        if not pp["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
            continue
        if not re.search(r"^\d{9}$", pp["pid"]):
            continue
        solution_2 += 1
    except:
        continue


print("solutions:", solution_1, solution_2)
