from math import prod

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def part_one(inp):
    def check_if_possible(line):
        game, dices = line.split(": ")
        _, id = game.split(" ")
        for dice_show in dices.split("; "):
            for dice_color in dice_show.split(", "):
                num, color = dice_color.split(" ")
                if int(num) > limits[color]:
                    return 0

        return int(id)

    limits = {"red": 12, "green": 13, "blue": 14}

    return sum([check_if_possible(line) for line in inp.split("\n")])


print("Test One:", part_one(test))

with open("02.inp") as fp:
    inp = fp.read()
print("Part One:", part_one(inp))


def part_two(inp):
    def set_min_possible(line):
        limits = {"red": 1, "green": 1, "blue": 1}
        game, dices = line.split(": ")
        _, id = game.split(" ")
        for dice_show in dices.split("; "):
            for dice_color in dice_show.split(", "):
                num, color = dice_color.split(" ")

                limits[color] = max(limits[color], int(num))

        return prod(limits.values())

    return sum([set_min_possible(line) for line in inp.split("\n")])

print("Test Two:", part_two(test))

with open("02.inp") as fp:
    inp = fp.read()
print("Part Two:", part_two(inp))