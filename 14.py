from icecream import ic

test = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

shifted = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""


def parse(inp):
    rows = inp.splitlines()
    return rows


def rotate_cw(m):
    # Rotates clockwise
    nm = tuple("".join(reversed(col)) for col in zip(*m))
    return nm


def roll(rows):
    # Moves everything to the right.
    rows = tuple("#".join("".join(sorted(r)) for r in row.split("#")) for row in rows)
    return rows


def calc(rows):
    return sum(x for row in rows for x, char in enumerate(row, 1) if char == "O")


def part_one(rows):
    rows = parse(rows)
    rows = rotate_cw(rows)
    rows = roll(rows)
    return calc(rows)


def part_two(rows, cycles=3):
    rows = parse(rows)
    rows = rotate_cw(rows)
    memo = dict()
    for c in range(cycles):
        if rows in memo:
            i = memo[rows] + (cycles - c) % (c - memo[rows])
            return calc(next(k for k, v in memo.items() if v == i))
        memo[rows] = c
        rows = rotate_cw(roll(rotate_cw(roll(rotate_cw(roll(rotate_cw(roll(rows))))))))


with open("14.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test))

print("Part One:", part_one(inp))

print("Test Two:", part_two(test, cycles=1000000000))

print("Test Two:", part_two(inp, cycles=1_000_000_000))
