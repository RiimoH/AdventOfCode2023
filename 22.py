from icecream import ic
from collections import namedtuple


test = """1,0,1~1,2,1
0,0,2~2,0,2
0,0,4~0,2,4
2,0,5~2,2,5
0,2,3~2,2,3
0,1,6~2,1,6
1,1,8~1,1,9"""


Point = namedtuple("Point", ["x", "y", "z"])


class Block:
    def __init__(self, st, ed):
        self.start: Point = Point(*st)
        self.end: Point = Point(*ed)

    def __lt__(self, other):
        return self.start.z < other.start.z

    def __repr__(self) -> str:
        return f"{str(self.start)} -> {str(self.end)}"


def parse(inp):
    blocks = []
    for line in inp.splitlines():
        st, ed = line.split("~")
        st = tuple(map(int, st.split(",")))
        ed = tuple(map(int, ed.split(",")))

        b = list(zip(st, ed))

        block = Block(tuple(map(min, b)), tuple(map(max, b)))
        blocks.append(block)
    return sorted(blocks)


def part_one(inp):
    blocks = parse(inp)
    ic(blocks)


def part_two(inp):
    ...


# with open("") as fp:
#     inp = fp.read()

print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
