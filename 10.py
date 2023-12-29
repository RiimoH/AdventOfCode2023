from icecream import ic
from math import prod

test = """.....
.S-7.
.|.|.
.L-J.
....."""

test2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

test3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

test4 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

test5 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

L, R, U, D = vectors = ((0, -1), (0, 1), (-1, 0), (1, 0))

dirs = {
    "|": (U, D),
    "-": (L, R),
    "L": (U, R),
    "J": (U, L),
    "7": (L, D),
    "F": (D, R),
    ".": 0,
}


def parse(inp):
    inp = inp.split("\n")

    board = dict()
    for r, line in enumerate(inp):
        for c, char in enumerate(line):
            if char == "S":
                s = (r, c)
            if char in dirs:
                board[(r, c)] = dirs[char]

    return s, board


def reverse_vector(vector):
    return tuple(map(prod, zip(vector, (-1, -1))))


def move_by_vector(pos, vector):
    return tuple(map(sum, zip(pos, vector)))


def get_vector(origin, destination):
    return (destination[0] - origin[0], destination[1] - origin[1])


def get_turn(last_vector, new_vector):
    # Right
    if (last_vector[1], -last_vector[0]) == new_vector:
        return 1

    # Left
    elif (-last_vector[1], last_vector[0]) == new_vector:
        return -1

    # STraigth
    else:
        return 0


def part_one(inp):
    pos, board = parse(inp)

    chains = []

    for vector in vectors:
        npos = move_by_vector(pos, vector)
        if board.get(npos, False):
            chains.append([pos, npos])

    steps = 2
    while True:
        poi = []
        new_chains = []
        for chain in chains:
            directions = board.get(chain[-1])
            d1, d2 = directions
            np1, np2 = move_by_vector(chain[-1], d1), move_by_vector(chain[-1], d2)
            if np1 == chain[-2] and np2 in board:
                new_chains.append(
                    chain
                    + [
                        np2,
                    ]
                )
                if np2 in poi:
                    return steps, new_chains, np2, board
                poi.append(np2)
            elif np1 in board and np2 == chain[-2]:
                new_chains.append(
                    chain
                    + [
                        np1,
                    ]
                )
                if np1 in poi:
                    return steps, new_chains, np1, board
                poi.append(np1)

        chains = new_chains
        steps += 1


def part_two(inp):
    _, chains, last_position, board = part_one(inp)

    # determine the whole loop
    chains = list(filter(lambda x: x[-1] == last_position, chains))

    whole_chain = chains[0] + list(reversed(chains[1][1:-1]))

    s = 0
    for i, (c1, r1) in enumerate(whole_chain):
        (c2, r2) = whole_chain[i - 1]
        s += c1 * r2 - r1 * c2

    A = s / 2
    R = len(whole_chain)
    return int(abs(A) + 1 - (R / 2))


with open("10.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test)[0])
# print("Test One-2:", part_one(test2)[0])

# print("Part One:", part_one(inp)[0])

print("Test Two.1 4", part_two(test3))
print("Test Two.2 8:", part_two(test4))
print("Test Two.3 10 :", part_two(test5))

print("Part Two:", part_two(inp))
