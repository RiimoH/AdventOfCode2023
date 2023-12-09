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


Subaction = namedtuple(
    "Subaction",
    ["target_lower", "target_upper", "origin_lower", "origin_upper", "calculation"],
)

Map = namedtuple(
    "Map", ["lower_bounds", "upper_bounds", "origin"]
)


def make_actions(inp):
    actions: List[Subaction] = []

    for action in inp:
        action = action[1:]
        subaction: List[Subaction] = list()
        for srange in action:
            srange = list(map(int, srange.split()))
            sa = Subaction(
                srange[0],
                srange[0] + srange[2] - 1,
                srange[1],
                srange[1] + srange[2] - 1,
                srange[0] - srange[1],
            )
            subaction.append(sa)
        subaction.sort()

        actions.append(subaction)

    return actions


def part_two(inp):
    inp = inp.split("\n\n")
    seed, inp = inp[0], inp[1:]
    inp = list(map(lambda x: x.split("\n"), inp))

    actions = make_actions(inp)

    raw_seeds = list(map(int, seed.split()[1:]))
    seeds = []
    while raw_seeds:
        start = raw_seeds.pop(0)
        srange = raw_seeds.pop(1)

        seeds.append(Map(start, start+srange-1, start))

    ic(actions)
    ic(seeds)
    return

    while seeds:
        sstart, srange, seeds = seeds[0], seeds[1], seeds[2:]
        for seed in range(sstart, sstart + srange):
            for action in actions:
                for action_range in action:
                    if 0 <= seed - action_range[1] < action_range[2]:
                        seed = seed + action_range[0] - action_range[1]
                        break

            min_location = min(min_location, seed)

    return min_location


with open("05.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
