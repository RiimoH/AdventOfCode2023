from icecream import ic


test = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


def parse(inp):
    board = {}
    for r, row in enumerate(inp.splitlines()):
        for c, char in enumerate(row):
            board[(r, c)] = char if char != "S" else "."
            if char == "S":
                s = (r, c)
    return board, s


dirs = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)


def part_one(inp, step_num=1):
    board, (sr, sc) = parse(inp)

    visited = {
        (0, sr, sc),  # 1 is odd, 0 is even
    }

    steps = [
        (sr, sc),
    ]

    for step in range(1, step_num + 1):
        even_odd = step % 2
        new_steps = list()
        for sr, sc in steps:
            for dr, dc in dirs:
                npos = sr + dr, sc + dc
                if board.get(npos, "#") == "#":
                    continue
                if (even_odd, *npos) not in visited and npos not in new_steps:
                    new_steps.append(npos)
                visited.add(
                    (even_odd, *npos),
                )
        steps = new_steps

        # l = [list(r) for r in inp.splitlines()]
        # for eo, r, c in visited:
        #     if eo == even_odd:
        #         l[r][c] = "O"
        # s = "\n".join(["".join(r) for r in l])
        # print(s)

    return len(list(filter(lambda x: x[0] == 0, visited)))


def part_two(inp):
    ...


with open("21.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test, step_num=6))


print("Part One:", part_one(inp, step_num=64))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
