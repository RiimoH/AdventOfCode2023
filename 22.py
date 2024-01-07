from icecream import ic
from collections import namedtuple


test = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


Point = namedtuple("Point", ["x", "y", "z"])


class Block:
    def __init__(self, points):
        self.points = sorted(points, key=lambda p: p.z)
        self.supports = set()
        self.supported_by = set()

    def __lt__(self, other):
        return self.points[0].z < other.points[0].z

    # def __repr__(self) -> str:
    #     return f"Block {self.name}"

    # def expr(self):
    #     return f"Block {self.name}, supported by {self.supported_by}"


def parse(inp):
    blocks = []
    for line in inp.splitlines():
        st, et = line.split("~")
        (sx, sy, sz), (ex, ey, ez) = map(int, st.split(",")), map(int, et.split(","))

        b = [
            Point(ix, iy, iz)
            for ix in range(min(sx, ex), max(sx, ex) + 1)
            for iy in range(min(sy, ey), max(sy, ey) + 1)
            for iz in range(min(sz, ez), max(sz, ez) + 1)
        ]

        block = Block(b)
        blocks.append(block)
    return sorted(blocks)


def part_one(inp):
    blocks = parse(inp)

    settled_points = set()
    settled_blocks = dict()

    for block in blocks:
        while block.points[0].z > 1:
            new_points = [
                Point(point.x, point.y, point.z - 1) for point in block.points
            ]

            supporting_points = settled_points.intersection(new_points)
            if supporting_points:
                for s in supporting_points:
                    settled_blocks[s].supports.add(block)
                    block.supported_by.add(settled_blocks[s])
                break

            block.points = new_points

        settled_points.update(block.points)
        for p in block.points:
            settled_blocks[p] = block

    disintegration = set()
    keep_at_any_cost = set()
    for block in blocks:
        if not block.supports:
            disintegration.add(block)
        if len(block.supported_by) > 1:
            disintegration.update(block.supported_by)
        elif len(block.supported_by) == 1:
            keep_at_any_cost.update(block.supported_by)

    disintegration.difference_update(keep_at_any_cost)

    return len(disintegration)


def part_two(inp):
    blocks = parse(inp)

    settled_points = set()
    settled_blocks = dict()

    for block in blocks:
        while block.points[0].z > 1:
            new_points = [
                Point(point.x, point.y, point.z - 1) for point in block.points
            ]

            supporting_points = settled_points.intersection(new_points)
            if supporting_points:
                for s in supporting_points:
                    settled_blocks[s].supports.add(block)
                    block.supported_by.add(settled_blocks[s])
                break

            block.points = new_points

        settled_points.update(block.points)
        for p in block.points:
            settled_blocks[p] = block

    max_falling = 0
    for block in blocks:
        queue = [*block.supports]

        while queue:
            b = queue.pop()
            ...


with open("22.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test))

print("Part One:", part_one(inp))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
