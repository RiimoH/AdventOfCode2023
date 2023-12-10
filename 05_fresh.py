from icecream import ic
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


def parse_maps(maps):
    all_maps = []
    for map in maps:
        _, *ranges = map.split("\n")
        ranges = [
            [(x) for x in r.split()] for r in ranges
        ]        
        all_maps.append(ranges)
    
    return all_maps



def part_two(inp):
    inp = inp.split("\n\n")
    seed, maps = inp[0], inp[1:]

    seeds = []
    seed = seed.split()[1:]
    while seed:
        x = int(seed.pop(0))
        y = int(seed.pop(0))
        seeds.append(range(x, x + y))

    maps = parse_maps(maps)

    ic(maps)
    ic(seeds)

    for map in maps:
        new_seeds = list()
        for action in map:
            for seed in seeds:
                if seed 
                if action[1] in seed:
                    ...


with open("05.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

print("Test Two:", part_two(test))
