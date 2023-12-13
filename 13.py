from icecream import ic


test = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def part_one(inp):
    def parse(inp):
        inp = inp.split("\n\n")
        inp = [x.split("\n") for x in inp]
        return inp

    def find_horizontal_reflection(inp):
        for i in range(len(inp) - 1):
            o, u = i, i + 1

            while inp[o] == inp[u]:
                o -= 1
                u += 1

                if o < 0 or u >= len(inp):
                    return i + 1
        else:
            return -1

    def find_vertical_reflection(inp):
        inp = ["".join(x) for x in zip(*inp)]
        return find_horizontal_reflection(inp)

    inp = parse(inp)

    ts = 0
    for part in inp:
        x = find_horizontal_reflection(part)
        if x >= 0:
            ts += x * 100
            continue
        x = find_vertical_reflection(part)
        if x >= 0:
            ts += x
            continue

    return ts


def part_two(inp):
    def parse(inp):
        inp = inp.split("\n\n")
        inp = [x.split("\n") for x in inp]
        return inp

    def find_horizontal_reflection(inp):
        for i in range(len(inp) - 1):
            o, u = i, i + 1
            smudge = False
            while True:
                comp = compare(inp[o], inp[u])
                if comp > 1:
                    break
                elif comp == 1:
                    if smudge:
                        break
                    else:
                        smudge = True
                        
                o -= 1
                u += 1

                if o < 0 or u >= len(inp):
                    if smudge:
                        return i + 1
                    else:
                        break
        else:
            return -1

    def find_vertical_reflection(inp):
        inp = ["".join(x) for x in zip(*inp)]
        return find_horizontal_reflection(inp)

    inp = parse(inp)

    def compare(x, y):
        comp = [1 if x[idx] != y[idx] else 0 for idx in range(len(x))]
        return sum(comp)


    ts = 0
    for part in inp:
        x = find_horizontal_reflection(part)
        if x >= 0:
            ts += x * 100
            continue
        x = find_vertical_reflection(part)
        if x >= 0:
            ts += x
            continue

    return ts



with open("13.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

print("Test Two:", part_two(test))

print("Part Two:", part_two(inp))
