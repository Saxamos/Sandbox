puzzle = open("8.txt").read().split("\n")

# 1
solution_1 = 0
for el in puzzle:
    code = el.split(" | ")[1].split(" ")
    for c in code:
        if len(c) in [2, 3, 4, 7]:
            solution_1 += 1

# 2
solution_2 = 0
for el in puzzle:
    digits, code = el.split(" | ")
    deux_trois_cinq = []
    zero_six_neuf = []
    for d in digits.split(" "):
        d = set(d)
        if len(d) == 2:
            un = d
        elif len(d) == 4:
            quatre = d
        elif len(d) == 3:
            sept = d
        elif len(d) == 7:
            huit = d
        elif len(d) == 5:
            deux_trois_cinq += [d]
        else:
            zero_six_neuf += [d]

    for d in digits.split(" "):
        top = sept - un
        mid_bot = (
            set.intersection(deux_trois_cinq[0], deux_trois_cinq[1], deux_trois_cinq[2])
            - top
        )
        mid = set.intersection(mid_bot, quatre)
        bot = mid_bot - mid
        trois = set.union(top, mid, bot, un)
        topleft = quatre - un - mid
        for el1 in zero_six_neuf:
            if el1 == set.union(top, mid, bot, topleft, un):
                neuf = el1
        botleft = huit - neuf
        zero = set.union(top, bot, topleft, botleft, un)
        for el1 in zero_six_neuf:
            if el1 != zero and el1 != neuf:
                six = el1
        botright = six - top - mid - bot - botleft - topleft
        topright = un - botright
        cinq = set.union(top, topleft, mid, botright, bot)
        deux = set.union(top, topright, mid, botleft, bot)

    mapper = {
        "0": zero,
        "1": un,
        "2": deux,
        "3": trois,
        "4": quatre,
        "5": cinq,
        "6": six,
        "7": sept,
        "8": huit,
        "9": neuf,
    }
    decode = ""
    for c in code.split(" "):
        c = set(c)
        for k, v in mapper.items():
            if c == v:
                decode += k
    print(decode)
    solution_2 += int(decode)

print("solutions:", solution_1, solution_2)
