from icecream import ic
import re


test = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


def parse(inp):
    lines = inp.splitlines()
    board = {(r, c): char for r, row in enumerate(lines) for c, char in enumerate(row)}

    start = (0, 1)
    goal = (len(lines) - 1, len(lines[0]) - 2)

    return board, start, goal


def part_one(inp):
    def generate_sections(section):
        pc, pr = section[-1]

        for dc, dr in dirs.values():
            npos = pc + dc, pr + dr

            if npos in section:
                continue

            if npos in crossings:
                sections.append((section + [npos], len(section)))
                continue

            nt = board.get(npos, "#")

            if nt == "." or (nt in dirs.keys() and (dr, dc) == dirs[nt]):
                generate_sections(section + [npos])

    def generate_crossings(crossings):
        for (r, c), tile in board.items():
            if tile == ".":
                neighbors = []
                for dr, dc in dirs.values():
                    if (nt := board.get((r + dr, c + dc), "#")) != "#":
                        neighbors.append(nt)

                if len(neighbors) > 2:
                    crossings.add((r, c))

        return crossings

    dirs = {
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
        "^": (-1, 0),
    }

    board, start, goal = parse(inp)
    sections = []

    crossings = generate_crossings(
        {
            start,
            goal,
        }
    )
    ic(crossings)
    for s in crossings:
        generate_sections(
            [s],
        )

    ic(sections)


def part_two(inp):
    ...


with open("23.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
