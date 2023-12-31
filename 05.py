from icecream import ic
import math
from collections import namedtuple
from typing import List

test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def parse(inp):
    inp = inp.split("\n\n")
    inp = list(map(lambda x: x.split("\n"), inp))

    seeds = {}

    for seed in inp[0][0].split()[1:]:
        seed = int(seed)
        seeds[seed] = {0: seed}

    what = []
    actions = []

    for action in inp[1:]:
        w, action = action[0], action[1:]
        action = list(map(lambda x: list(map(int, x.split())), action))
        what.append(w)
        actions.append(action)

    return seeds, actions

    # Setup done, do all the seeds


def part_one(inp):
    seeds, actions = parse(inp)

    for seed, dseed in seeds.items():
        for i, action in enumerate(actions):
            for action_range in action:
                if 0 <= dseed[i] - action_range[1] < action_range[2]:
                    dseed[i + 1] = dseed[i] + action_range[0] - action_range[1]
                    break
            else:
                dseed[i + 1] = dseed[i]

    return min([v[7] for v in seeds.values()])


def make_actions(inp):
    actions = []

    for tmap in inp:
        tmap = tmap.splitlines()
        tmap = tmap[1:]
        sactions = []
        for sa in tmap:
            drs, srs, rl = list(map(int, sa.split()))
            sactions.append(
                (
                    range(srs, srs + rl),
                    range(drs, drs + rl),
                )
            )

        actions.append(sactions)

    return actions


def part_two(inp):
    inp = inp.split("\n\n")
    seed, actions = inp[0], inp[1:]

    seed = seed.split()[1:]
    seeds = []
    while seed:
        st = int(seed.pop(0))
        ra = int(seed.pop(0))

        seeds.append(range(st, st + ra))

    actions = make_actions(actions)

    for action in actions:
        new_seeds = []
        for tmap in action:
            remaining_seeds = []
            for seedr in seeds:
                if tmap[-1] < seedr[0] or tmap[0] > seedr[-1]:
                    remaining_seeds.append(seedr)

                elif tmap[-1] < seedr[-1] and tmap[0] < seedr[0]:
                    # starts below and ends inside
                    stmap = seedr.index(tmap[0])
                    new_seeds.append(seedr[: stmap + 1])
                    remaining_seeds.append(seedr[stmap + 1 :])

                elif tmap[-1] > seedr[-1] and tmap[0] > seedr[0]:
                    # Starts inside and extends beyond
                    stmap = seedr.index(tmap[0])
                    remaining_seeds.append(seedr[:stmap])
                    new_seeds.append(seedr[stmap:])

                elif tmap[-1] < seedr[-1] and tmap[0] > seedr[0]:
                    # Is completly inside
                    stmap = seedr.index(tmap[0])
                    etmap = seedr.index(tmap[-1])
                    remaining_seeds.append(seedr[:stmap])
                    remaining_seeds.append(seedr[etmap + 1 :])
                    new_seeds.append(seedr[stmap : etmap + 1])

            seeds = remaining_seeds
        seeds.extend(new_seeds)

    return seeds

    # range(max(x[0], y[0]), min(x[-1], y[-1]) + 1)

    # while seeds:
    #     sstart, srange, seeds = seeds[0], seeds[1], seeds[2:]
    #     for seed in range(sstart, sstart + srange):
    #         for action in actions:
    #             for action_range in action:
    #                 if 0 <= seed - action_range[1] < action_range[2]:
    #                     seed = seed + action_range[0] - action_range[1]
    #                     break

    #         min_location = min(min_location, seed)

    # return min_location


with open("05.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
