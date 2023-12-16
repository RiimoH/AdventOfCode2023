from icecream import ic


test = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

UP, DOWN, RIGHT, LEFT = DIRS = ((-1, 0), (1, 0), (0, 1), (0, -1))

dirs = {
    "/": {
        UP: RIGHT,
        LEFT: DOWN,
        DOWN: LEFT,
        RIGHT: UP,
    },
    "\\": {
        UP: LEFT,
        LEFT: UP,
        DOWN: RIGHT,
        RIGHT: DOWN,
    },
    "|": {
        UP: UP,
        DOWN: DOWN,
        RIGHT: (UP, DOWN),
        LEFT: (UP, DOWN),
    },
    "-": {
        LEFT: LEFT,
        RIGHT: RIGHT,
        UP: (LEFT, RIGHT),
        DOWN: (LEFT, RIGHT),
    },
    ".": {
        RIGHT: RIGHT,
        LEFT: LEFT,
        UP: UP,
        DOWN: DOWN,
    },
}


def parse(inp):
    inp = inp.splitlines()
    board = {(r, c): char for r, row in enumerate(inp) for c, char in enumerate(row)}

    width = len(inp[0])
    height = len(inp)
    return board, width, height


def part_one(board, v1=0, v2=-1, d1=RIGHT):
    visited = {}

    beams = [
        ((v1, v2), d1),
    ]

    while beams:
        pos, dir = beams.pop(0)
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])

        nt = board.get(new_pos, False)
        if nt is False:
            continue

        if new_pos in visited:
            if dir in visited[new_pos]:
                continue
            else:
                visited[new_pos].append(dir)
        else:
            visited[new_pos] = [
                new_pos,
            ]

        new_dir = dirs[nt][dir]
        if type(new_dir[0]) is tuple:
            for d in new_dir:
                beams.append((new_pos, d))
        else:
            beams.append((new_pos, new_dir))

    # lines = [list(line) for line in inp.splitlines()]
    # for pc, pr in visited.keys():
    #     lines[pc][pr] = "#"
    # for line in lines:
    #     print("".join(line))

    return len(visited)


def part_two(board, width, height):
    most_energy = 0

    for c in range(width):
        most_energy = max(most_energy, part_one(board, -1, c, DOWN))
        most_energy = max(most_energy, part_one(board, height, c, UP))

    for r in range(height):
        most_energy = max(most_energy, part_one(board, r, -1, RIGHT))
        most_energy = max(most_energy, part_one(board, r, height, LEFT))

    return most_energy


with open("16.inp") as fp:
    inp = fp.read()

test, wt, ht = parse(test)
inp, w, h = parse(inp)

print("Test One:", part_one(test))

ic.disable()
print("Part One:", part_one(inp))

print("Test Two:", part_two(test, wt, ht))

print("Part Two:", part_two(inp, w, h))
