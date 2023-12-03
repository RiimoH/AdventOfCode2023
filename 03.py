from colorama import Fore
from math import prod


test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

test2 = """12.......*..
+.........34
.......-12..
..78........
..*....60...
78.........9
.5.....23..$
8...90*12...
............
2.2......12.
.*.........*
1.1..503+.56"""

dirs = (
    (1, -1),
    (1, 0),
    (1, 1),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
)


def map_to_dict(inp):
    d = dict()
    for y, row in enumerate(inp.split("\n")):
        for x, char in enumerate(row):
            d[x, y] = char
    return d


def map_to_list(inp):
    l = inp.split("\n")
    return l


def part_one(inp):
    d = map_to_dict(inp)
    l = map_to_list(inp)
    part_numbers = []

    for (x, y), char in d.items():
        if char not in "0123456789.":
            for dx, dy in dirs:
                ix = x + dx
                iy = y + dy
                num = d.get((ix, iy), ".")
                if num.isdigit():
                    d[ix, iy] = "."
                    lix = 1
                    lnum = d.get((ix - lix, iy), ".")
                    while lnum.isdigit():
                        d[ix - lix, iy] = "."
                        num = lnum + num
                        lix += 1
                        lnum = d.get((ix - lix, iy), ".")

                    rix = 1
                    rnum = d.get((ix + rix, iy), ".")
                    while rnum.isdigit():
                        d[ix + rix, iy] = "."
                        num = num + rnum
                        rix += 1
                        rnum = d.get((ix + rix, iy), ".")

                    part_numbers.append(int(num))
    return sum(part_numbers)

def part_two(inp):
    d = map_to_dict(inp)
    l = map_to_list(inp)
    part_numbers = []

    for (x, y), char in d.items():
        if char in "*":
            numbers = list()
            for dx, dy in dirs:
                ix = x + dx
                iy = y + dy
                num = d.get((ix, iy), ".")
                if num.isdigit():
                    d[ix, iy] = "."
                    lix = 1
                    lnum = d.get((ix - lix, iy), ".")
                    while lnum.isdigit():
                        d[ix - lix, iy] = "."
                        num = lnum + num
                        lix += 1
                        lnum = d.get((ix - lix, iy), ".")

                    rix = 1
                    rnum = d.get((ix + rix, iy), ".")
                    while rnum.isdigit():
                        d[ix + rix, iy] = "."
                        num = num + rnum
                        rix += 1
                        rnum = d.get((ix + rix, iy), ".")

                    numbers.append(int(num))

            if len(numbers) == 2:
                part_numbers.append(prod(numbers))
    return sum(part_numbers)


print("Test One:", part_one(test))
print("Test One:", part_one(test2))

with open("03.inp") as fp:
    inp = fp.read()
print("Part One:", part_one(inp))

print("Test Two:", part_two(test))

with open("03.inp") as fp:
    inp = fp.read()
print("Part Two:", part_two(inp))
