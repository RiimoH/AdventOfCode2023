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
    rows = inp.split("\n")
    rows = ["#" * len(rows[0])] + rows
    return rows


def part_one(rows):
    total = 0
    for r, row in enumerate(rows):
        for c, tile in enumerate(row):
            if tile == "#":
                # shift all the rocks closer
                next_spot = r + 1

                for dr in range(r + 1, len(rows)):
                    if rows[dr][c] == "O":
                        total += len(rows) - next_spot
                        next_spot += 1
                    if rows[dr][c] == "#":
                        break

    return total


def rotate_matrix(m):
    nm = [list(reversed(col)) for col in zip(*m)]
    if "." in nm[0] or "O" in nm[0]:
        nm = ["#" * len(nm[0])] + nm
    return nm


def move_all(rows):
    new_rows = [[x if x == "#" else "." for x in row] for row in rows]
    for r, row in enumerate(rows):
        for c, tile in enumerate(row):
            if tile == "#":
                # shift all the rocks closer
                next_spot = r + 1

                for dr in range(r + 1, len(rows)):
                    if rows[dr][c] == "O":
                        new_rows[next_spot][c] = "O"
                        next_spot += 1
                    if rows[dr][c] == "#":
                        break
    return new_rows


def part_two(rows, cycles=3):
    def calc(rows):
        total = 0
        for r, row in enumerate(rows):
            print("".join(row), r)
            for c, tile in enumerate(row):
                if tile == "O":
                    total += len(rows) - r
        return total

    memo = {}
    for cycle in range(cycles):
        for i in range(4):
            rows = rotate_matrix(move_all(rows))

        state = "\n".join(["".join(row[1:-1]) for row in rows[1:-1]])
        if state in memo:
            print(state)
            return (cycle, memo[state], calc(rows))
        else:
            memo["\n".join(["".join(row) for row in rows])] = cycle

        # print(f"\nAfter {cycle+1} cycles:")
        # for row in rows:
        #     print("".join(row))
    return part_one(rows)


with open("14.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(parse(test)))

print("Part One:", part_one(parse(inp)))

print("Test Two:", part_two(parse(test), cycles=1_000_000_000))

# print("Test Two:", part_two(parse(inp)))
