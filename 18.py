from icecream import ic
from collections import namedtuple
from typing import List

test = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

Dig = namedtuple("Dig", ["dir", "steps", "rgb"])

DIR = dict(zip(("U", "R", "D", "L"), ((-1, 0), (0, 1), (1, 0), (0, -1))))


def parse(inp):
    instr = []
    for line in inp.splitlines():
        d, s, rgb = line.split()
        s = int(s)
        rgb = rgb.rstrip(")").lstrip("(")
        instr.append(Dig(d, s, rgb))
    return instr


def part_one(inp):
    def expand(c, r):
        for dc, dr in DIR.values():
            d = (c + dc, r + dr)
            if d not in visited and d not in inside:
                inside.add(d)
                expand(*d)

    instr: List[Dig] = parse(inp)
    sc, sr = 0, 0
    visited = {}
    inside = set()

    dirs, *_ = zip(*instr)
    dirs = "".join(dirs)
    if (
        sum(dirs.count(x) for x in ("UR", "RD", "DL", "LU"))
        - sum(dirs.count(x) for x in ("RU", "DR", "LD", "UL"))
        > 0
    ):
        # RIGHTS
        side = lambda p, s: (p[0] + s[1], p[1] - s[0])
    else:
        # LEFTS
        side = lambda p, s: (p[0] - s[1], p[1] + s[0])

    for dig in instr:
        for _ in range(dig.steps):
            sc += DIR[dig.dir][0]
            sr += DIR[dig.dir][1]
            inside.add(side((sc, sr), DIR[dig.dir]))
            visited[(sc, sr)] = dig.rgb

    inside.difference_update(visited.keys())
    flooded = inside.copy()
    while inside:
        cc, cr = c = inside.pop()
        for dc, dr in DIR.values():
            n = cc + dc, cr + dr
            if n not in flooded and n not in visited.keys():
                inside.add(n)
                flooded.add(n)

    dig = flooded.union(visited.keys())

    return len(dig)


def part_two(inp):
    ...


with open("18.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test))

print("Part One:", part_one(inp))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
