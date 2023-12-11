from icecream import ic

test = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def part_one(inp):
    def parse(inp):
        inp = inp.split("\n")
        image = {}

        # expand
        img = []
        for row in inp:
            if "#" not in row:
                img.append(row)
            img.append(row)

        inp = [list(x) for x in zip(*img)]

        img = []
        for row in inp:
            if "#" not in row:
                img.append(row)
            img.append(row)

        # map
        for r, row in enumerate(img):
            for c, char in enumerate(row):
                image[(r, c)] = char

        return image

    def find_shortest_paths(img):
        galaxies = {coords: dict() for coords, char in img.items() if char == "#"}

        galist = list(galaxies.keys())

        # I only need to look down, left and right
        shortest_distances = []

        for i, ga in enumerate(galist):
            for gb in galist[i + 1 :]:
                distance = abs(gb[0] - ga[0]) + abs(gb[1] - ga[1])
                # galaxies[ga][gb] = distance
                # galaxies[gb][ga] = distance
                shortest_distances.append(distance)

        return shortest_distances

    img = parse(inp)

    shortest_paths = find_shortest_paths(img)

    return sum(shortest_paths)


def part_two(inp, jump: int):
    def parse(inp):
        inp = inp.split("\n")
        image = {}

        col_jumps = set()
        row_jumps = set()
        # expand
        for r, row in enumerate(inp):
            if "#" not in row:
                row_jumps.add(r)

        flip = [list(x) for x in zip(*inp)]

        for c, row in enumerate(flip):
            if "#" not in row:
                col_jumps.add(c)

        # map
        for r, row in enumerate(inp):
            for c, char in enumerate(row):
                image[(r, c)] = char

        return image, col_jumps, row_jumps

    def find_shortest_paths(img, jump):
        galaxies = {coords: dict() for coords, char in img.items() if char == "#"}

        galist = list(galaxies.keys())

        # I only need to look down, left and right
        shortest_distances = []

        for i, ga in enumerate(galist):
            for gb in galist[i + 1 :]:
                distance = abs(gb[0] - ga[0]) + abs(gb[1] - ga[1])
                for x in row_jumps:
                    if min(ga[0], gb[0]) < x < max(ga[0], gb[0]):
                        distance += jump-1
                for y in col_jumps:
                    if min(ga[1], gb[1]) < y < max(ga[1], gb[1]):
                        distance += jump-1

                shortest_distances.append(distance)

        return shortest_distances

    img, col_jumps, row_jumps = parse(inp)

    shortest_paths = find_shortest_paths(img, jump)

    return sum(shortest_paths)


with open("11.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

print("Test Two:", part_two(test, 10))
print("Test Two:", part_two(test, 100))

print("Part Two:", part_two(inp, 1_000_000))
