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

            if npos in crossings:
                sections.append(section)
                continue

            t = board.get(npos, "#")
            if t == "." or (t in dirs.keys() and (dr, dc) == dirs[t]):
                tiles_around.append((npos, t))

        if len(tiles_around) <= 2:
            for npos, t in tiles_around:
                if npos not in section:
                    section.append(npos)
            generate_sections(section)

        else:
            sections.append(
                (len(section), section[0], section[-1]),
            )
            generate_sections(section[-1])

    def generate_crossings(crossings):
        for (r, c), tile in board.items():
            if tile == ".":
                neighbors = []
                for dr, dc in dirs.values():
                    if (nt := board.get((r + dr, c + dc), "#")) != "#":
                        # if nt == "." or (nt in dirs.keys() and (dr, dc) == dirs[nt]):
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
        }
    )
    for s in crossings:
        generate_sections(
            [s],
        )


def part_two(inp):
    ...


with open("23.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
