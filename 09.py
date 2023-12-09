from icecream import ic


test = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def parse(inp):
    lines = []
    for line in inp.split("\n"):
        line = list(map(int, line.split()))
        lines.append(line)

    return lines


def calc_next_value(line):
    if all(map(lambda x: x == 0, line)):
        return 0

    next_line = [line[i + 1] - line[i] for i in range(len(line)-1)]

    return line[-1] + calc_next_value(next_line)


def calc_earlier_value(line):
    if all(map(lambda x: x == 0, line)):
        return 0

    next_line = [line[i + 1] - line[i] for i in range(len(line)-1)]

    return line[0] - calc_earlier_value(next_line)


def part_one(inp):
    lines = parse(inp)

    next_values = []
    for line in lines:
        next_values.append(calc_next_value(line))
    return sum(next_values)


def part_two(inp):
    lines = parse(inp)

    next_values = []
    for line in lines:
        next_values.append(calc_earlier_value(line))
    return sum(next_values)

with open("09.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

print("Test Two:", part_two(test))

print("Part Two:", part_two(inp))
