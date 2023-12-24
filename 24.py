from icecream import ic


test = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


def parse(inp):
    drops = []
    for line in inp.splitlines():
        pos, vec = line.split(" @ ")
        pos = [int(x) for x in pos.split(", ")]
        vec = [int(x) for x in vec.split(", ")]
        drops.append(
            (
                tuple(pos),
                tuple(vec),
            )
        )

    return drops


def part_one(inp, x_left=7, x_right=27):
    drops = parse(inp)
    ic(drops)

    intersecting = 0

    for i, ((px, py, pz), (vx, vy, vz)) in enumerate(drops[:-1]):
        for (ox, oy, oz), (qx, qy, qz) in drops[i + 1 :]:
            m1 = vy / vx
            m2 = qy / qx

            b1 = (x_left - px) * m1 + py
            b2 = (x_left - ox) * m2 + oy

            

            # pyl = (x_left - px) / vx * vy + py
            # oyl = -ox / qx * qy + oy

            # pyr = (x_right - px) / vx * vy + py
            # oyr = (x_right - ox) / qx * qy + oy

            # if (pyl > oyl and pyr < oyr) or (pyl < oyl and pyr > oyr):
            #     intersecting += 1

    return intersecting


def part_two(inp):
    ...


# with open("") as fp:
#     inp = fp.read()

print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
