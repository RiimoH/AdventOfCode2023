from icecream import ic
from queue import PriorityQueue
import math

# test = """2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533"""

test = """111111111111
999999999991
999999999991
999999999991
999999999991"""


def parse(inp):
    lines = inp.splitlines()
    return (
        {(c, r): int(v) for r, row in enumerate(lines) for c, v in enumerate(row)},
        len(lines[0]) - 1,
        len(lines) - 1,
    )


def part_one(board, tc, tr):
    pq = PriorityQueue()

    pq.put(
        (0, 0, 0, 1, 1, 0),
    )

    pq.put(
        (0, 0, 0, 1, 0, 1),
    )

    visited = {
        (0, 0, 0, 1, 0): 0,
        (0, 0, 1, 0, 0): 0,
    }

    while pq:
        heatloss, cc, cr, walked, vc, vr = pq.get()
        nc, nr = cc + vc, cr + vr
        if (nc, nr) not in board:
            continue

        heatloss += board[(nc, nr)]
        if (nc, nr) == (tc, tr):
            return heatloss

        if heatloss >= visited.get((nc, nr, vc, vr, walked), math.inf):
            continue
        else:
            visited[(nc, nr, vc, vr, walked)] = heatloss

        # STRAIGHT
        if walked < 3:
            pq.put(
                (
                    heatloss,
                    nc,
                    nr,
                    walked + 1,
                    vc,
                    vr,
                ),
            )
        # LEFT TURN
        pq.put(
            (
                heatloss,
                nc,
                nr,
                1,
                vr,
                -vc,
            )
        )
        # RIGHT TURN
        pq.put(
            (
                heatloss,
                nc,
                nr,
                1,
                -vr,
                vc,
            )
        )

    else:
        return 0


def part_two(board, tc, tr):
    pq = PriorityQueue()

    pq.put(
        (0, 0, 0, 1, 1, 0),
    )

    pq.put(
        (0, 0, 0, 1, 0, 1),
    )

    visited = {
        (0, 0, 0, 1, 0): 0,
        (0, 0, 1, 0, 0): 0,
    }

    while pq:
        heatloss, cc, cr, walked, vc, vr = pq.get()
        nc, nr = cc + vc, cr + vr
        if (nc, nr) not in board:
            continue

        heatloss += board[(nc, nr)]
        if (nc, nr) == (tc, tr) and walked >= 4:
            return heatloss

        if heatloss >= visited.get((nc, nr, vc, vr, walked), math.inf):
            continue
        else:
            visited[(nc, nr, vc, vr, walked)] = heatloss

        # STRAIGHT
        if walked <= 9:
            pq.put(
                (
                    heatloss,
                    nc,
                    nr,
                    walked + 1,
                    vc,
                    vr,
                ),
            )
        # LEFT TURN
        if walked > 3:
            pq.put(
                (
                    heatloss,
                    nc,
                    nr,
                    1,
                    vr,
                    -vc,
                )
            )
            # RIGHT TURN
            pq.put(
                (
                    heatloss,
                    nc,
                    nr,
                    1,
                    -vr,
                    vc,
                )
            )

    else:
        return 0


test, ttc, ttr = parse(test)

with open("17.inp") as fp:
    inp, tc, tr = parse(fp.read())

# print("Test One:", part_one(test, ttc, ttr))

# print("Part One:", part_one(inp, tc, tr))

print("Test Two:", part_two(test, ttc, ttr))

print("Part Two:", part_two(inp, tc, tr))
