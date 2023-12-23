from icecream import ic

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
        pr, pc = section[-1]

        for dr, dc in dirs.values():
            npos = pr + dr, pc + dc

            if npos in section:
                continue

            if npos in crossings:
                s = sections.get(section[0], dict())
                s[npos] = len(section)
                sections[section[0]] = s
                return

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

    def find_combinations(route, steps=0):
        if route[-1] == goal:
            routes.append(steps)
            return

        for (target), step in sections[route[-1]].items():
            if target in route:
                continue

            find_combinations(route + [target], steps + step)

    dirs = {
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
        "^": (-1, 0),
    }

    board, start, goal = parse(inp)
    sections = {}

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
    ic(goal)
    routes = []
    find_combinations([start])

    return max(routes)


def part_two(inp):
    def generate_sections(section):
        pr, pc = section[-1]

        for dr, dc in dirs.values():
            npos = pr + dr, pc + dc

            if npos in section:
                continue

            if npos in crossings:
                s = sections.get(section[0], dict())
                s[npos] = len(section)
                sections[section[0]] = s
                return

            nt = board.get(npos, "#")

            if nt == "." or nt in dirs.keys() :
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

    def find_combinations(route, steps=0):
        if route[-1] == goal:
            routes.append(steps)
            return

        for (target), step in sections[route[-1]].items():
            if target in route:
                continue

            find_combinations(route + [target], steps + step)

    dirs = {
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
        "^": (-1, 0),
    }

    board, start, goal = parse(inp)
    sections = {}

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
    ic(goal)
    routes = []
    find_combinations([start])

    return max(routes)


with open("23.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test))

ic.disable()
print("Part One:", part_one(inp))

ic.enable()
print("Test Two:", part_two(test))

ic.disable()
print("Part Two:", part_two(inp))
