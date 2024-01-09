from collections import namedtuple
from icecream import ic
from sympy import solve, Eq, symbols


test = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

Point = namedtuple("Point", ["x", "y", "z"])


def parse(inp):
    drops = []
    for line in inp.splitlines():
        pos, vec = line.split(" @ ")
        pos = Point(*[int(x) for x in pos.split(", ")])
        vec = Point(*[int(x) for x in vec.split(", ")])
        drops.append((pos, vec))

    return drops


def is_intersecting(p1, p2, n1, n2):
    try:
        a = n1.y / n1.x
        b = n2.y / n2.x

        c = (-p1.x / n1.x) * n1.y + p1.y
        d = (-p2.x / n2.x) * n2.y + p2.y

        x = (d - c) / (a - b)
        y = a * x + c

        return x, y
    except:
        return False, False


def check_time(x_intersect, p1, p2, n1, n2):
    x1 = (x_intersect - p1.x) / n1.x
    x2 = (x_intersect - p2.x) / n2.x
    return x1 >= 0 and x2 >= 0


def part_one(inp, lim_low=7, lim_high=27):
    drops = parse(inp)
    intersecting = 0

    for i, (p1, n1) in enumerate(drops[:-1]):
        for p2, n2 in drops[i + 1 :]:
            ic(p1, n1, p2, n2)
            x, y = ic(is_intersecting(p1, p2, n1, n2))
            if x and y:
                if lim_low <= x <= lim_high and lim_low <= y <= lim_high:
                    if ic(check_time(x, p1, p2, n1, n2)):
                        intersecting += 1

    return intersecting


def part_two(inp):
    drops = parse(inp)

    equations = []
    for drop in drops[:10]:
        xr, yr, zr, vxr, vyr, vzr = symbols("rx ry rz vrx vry vrz")
        (x, y, z), (vx, vy, vz) = drop
        equations.extend(
            [
                Eq((xr - x) * (vy - vyr), (yr - y) * (vx - vxr)),
                Eq((yr - y) * (vz - vzr), (zr - z) * (vy - vyr)),
            ]
        )

    solutions = solve(equations, dict=True)
    if len(solutions) == 1:
        sol = solutions[0]
        return sum([sol[xr], sol[yr], sol[zr]])


with open("24.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))
# ic.disable()
# print("Part One:", part_one(inp, lim_low=200000000000000, lim_high=400000000000000))

print("Test Two:", part_two(test))

print("Part Two:", part_two(inp))
