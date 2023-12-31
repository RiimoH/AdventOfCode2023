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
                    range(srs, srs + rl + 1),
                    range(drs, drs + rl + 1),
                )
            )

        actions.append(sactions)

    return actions


def part_two(inp):
    inp = inp.split("\n\n")
    seed, x2ymaps = inp[0], inp[1:]

    seed = seed.split()[1:]
    all_seed_ranges = []
    while seed:
        st = int(seed.pop(0))
        ra = int(seed.pop(0))

        all_seed_ranges.append(range(st, st + ra))

    x2ymaps = make_actions(x2ymaps)

    for x2ymap in x2ymaps:
        new_seeds = []
        for som in x2ymap:
            untouched_seeds = []
            for csr in all_seed_ranges:
                if csr[-1] < som[0][0] or csr[0] > som[0][-1]:
                    # csr is outside som
                    untouched_seeds.append(csr)

                elif csr[0] >= som[0][0] and csr[-1] > som[0][-1]:
                    # csr starts in/with som and extends beyond
                    smap = som[0].index(csr[0])
                    emap = csr.index(som[0][-1])

                    new_seeds.append(som[1][smap:])
                    untouched_seeds.append(csr[emap + 1 :])

                elif csr[0] < som[0][0] and csr[-1] <= som[0][-1]:
                    # csr starts before som and extends to/into it
                    smap = csr.index(som[0][0])
                    emap = som[0].index(csr[-1])

                    untouched_seeds.append(csr[:smap])
                    new_seeds.append(som[1][: emap + 1])

                elif csr[0] >= som[0][0] and csr[-1] <= som[0][-1]:
                    # csr is complettely contained
                    stmap = som[0].index(csr[0])
                    etmap = som[0].index(csr[-1])
                    new_seeds.append(som[1][stmap : etmap + 1])

                elif csr[0] < som[0][0] and csr[-1] > som[0][-1]:
                    # csr completely contains som
                    stmap = csr.index(som[0][0])
                    etmap = csr.index(som[0][-1])

                    new_seeds.append(som[1])
                    untouched_seeds.append(csr[:stmap])
                    untouched_seeds.append(csr[etmap + 1 :])

                else:
                    ic(csr, som, "Mistake")

            all_seed_ranges = untouched_seeds
        all_seed_ranges.extend(new_seeds)

    return sorted(all_seed_ranges, key=lambda x: x[0])[0][0]

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

print("Part Two:", part_two(inp))
