from collections import defaultdict

import numpy

puzzle = open("20.txt").read().split("\n\n")

tile_dict = {}
for tile in puzzle:
    tile = tile.split("\n")
    index = int(tile[0][-5:-1])
    array = numpy.zeros((10, 10))
    for index_row, row in enumerate(tile[1:]):
        for index_col, col in enumerate(row):
            if col == "#":
                array[index_row, index_col] = 1
    tile_dict[index] = array


# 1
def _check(current, a, b, c, d):
    if numpy.array_equal(current, a):
        return 1
    elif numpy.array_equal(current, b):
        return 2
    elif numpy.array_equal(current, c):
        return 3
    elif numpy.array_equal(current, d):
        return 4


keys = list(tile_dict.keys())
neighbors_count = defaultdict(int)
neighbors_tbrl = {k: [0, 0, 0, 0] for k in keys}

for i in range(len(keys)):
    current_key = keys[i]
    tile = tile_dict[current_key]
    current_top, current_bot, current_right, current_left = (
        tile[0],
        tile[-1],
        tile[:, -1],
        tile[:, 0],
    )
    for key in keys:
        if key == current_key:
            continue
        top, bot, right, left = (
            tile_dict[key][0],
            tile_dict[key][-1],
            tile_dict[key][:, -1],
            tile_dict[key][:, 0],
        )
        ret = None

        if _check(current_bot, top, numpy.flip(left), numpy.flip(bot), right):
            ret = _check(current_bot, top, numpy.flip(left), numpy.flip(bot), right)
            neighbors_tbrl[current_key][1] = (key, ret, False)
        elif _check(current_right, left, bot, numpy.flip(right), numpy.flip(top)):
            ret = _check(current_right, left, bot, numpy.flip(top), numpy.flip(right))
            neighbors_tbrl[current_key][2] = (key, ret, False)
        elif _check(current_top, bot, numpy.flip(right), numpy.flip(top), left):
            ret = _check(current_top, bot, numpy.flip(right), numpy.flip(top), left)
            neighbors_tbrl[current_key][0] = (key, ret, False)
        elif _check(current_left, right, top, numpy.flip(left), numpy.flip(bot)):
            ret = _check(current_left, right, top, numpy.flip(bot), numpy.flip(left))
            neighbors_tbrl[current_key][3] = (key, ret, False)
        elif _check(current_bot, numpy.flip(top), left, bot, numpy.flip(right)):
            ret = _check(current_bot, numpy.flip(top), left, bot, numpy.flip(right))
            neighbors_tbrl[current_key][1] = (key, ret, True)
        elif _check(current_right, numpy.flip(left), numpy.flip(bot), right, top):
            ret = _check(current_right, numpy.flip(left), numpy.flip(bot), top, right)
            neighbors_tbrl[current_key][2] = (key, ret, True)
        elif _check(current_top, numpy.flip(bot), right, top, numpy.flip(left)):
            ret = _check(current_top, numpy.flip(bot), right, top, numpy.flip(left))
            neighbors_tbrl[current_key][0] = (key, ret, True)
        elif _check(current_left, numpy.flip(right), numpy.flip(top), left, bot):
            ret = _check(current_left, numpy.flip(right), numpy.flip(top), bot, left)
            neighbors_tbrl[current_key][3] = (key, ret, True)

        if ret:
            neighbors_count[current_key] += 1

solution_1 = 1
for k, v in neighbors_count.items():
    if v == 2:
        solution_1 *= k

# 2
square_size = int(len(puzzle) ** (1 / 2))
square = [[None] * square_size for _ in range(square_size)]
for k, v in neighbors_tbrl.items():
    if v[0] == 0 and v[3] == 0:
        col, row = 0, 0
        square[col][row] = (k, 1, False)
        t, b, r, l = v
        break


def _flip(fingerprint):
    return fingerprint[0], fingerprint[1], not fingerprint[2]


def _convert(tbrl, rotation, is_flip):
    t, b, r, l = tbrl
    if rotation == 1:
        if not is_flip:
            return t, b, r, l
        else:
            return _flip(t), _flip(b), _flip(r), _flip(l)
    elif rotation == 2:
        if not is_flip:
            return l, r, t, b
        else:
            return _, _, _, _
    elif rotation == 3:
        if not is_flip:
            return b, t, l, r
        else:
            return _, _, _, _
    elif rotation == 4:
        if not is_flip:
            return r, _, _, _
        else:
            return _, _, _, _


while row < square_size:
    if t and row > 0 and not square[row - 1][col]:
        square[row - 1][col] = t
    if b and row + 1 < square_size and not square[row + 1][col]:
        square[row + 1][col] = b
    if r and col + 1 < square_size and not square[row][col + 1]:
        square[row][col + 1] = r
    if l and col > 0 and not square[row][col - 1]:
        square[row][col - 1] = l

    if col + 1 < square_size:
        col += 1
    else:
        col = 0
        row += 1
        if row == square_size:
            break

    tile_fingerprint = square[row][col]
    rotation = tile_fingerprint[1]
    is_flip = tile_fingerprint[2]

    t, b, r, l = _convert(neighbors_tbrl[tile_fingerprint[0]], rotation, is_flip)

"""
2971    1489    1171
2729    1427    2473
1951    2311    3079
"""

solution_2 = 0

print("solutions:", solution_1, solution_2)
