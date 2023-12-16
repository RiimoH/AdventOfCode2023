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
    return board


def part_one(inp):
    board = parse(inp)
    visited = {
        (0, 0): [
            RIGHT,
        ]
    }

    beams = [
        ((0, 0), RIGHT),
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
        ic((dir, new_dir, new_pos, nt))
        if type(new_dir[0]) is tuple:
            for d in new_dir:
                beams.append((new_pos, d))
        else:
            beams.append((new_pos, new_dir))

    lines = [list(line) for line in inp.splitlines()]
    for pc, pr in visited.keys():
        lines[pc][pr] = "#"
    for line in lines:
        print("".join(line))

    return len(visited)


def part_two(inp):
    ...


with open("16.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test))

ic.disable()
print("Part One:", part_one(inp))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
