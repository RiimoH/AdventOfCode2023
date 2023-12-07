from icecream import ic
import math


test = """Time:      7  15   30
Distance:  9  40  200"""

inp = """Time:        53     91     67     68
Distance:   250   1330   1081   1025"""



def parse(inp):
    t, d = inp.split('\n')
    t = t.split()
    t = list(map(int, t[1:]))

    d = d.split()
    d = list(map(int, d[1:]))

    return t, d

def part_one(inp):
    t, d = parse(inp)

    wins = []

    for i, race in enumerate(t):
        win = 0
        for hold in range(race):
            if (race-hold)*hold > d[i]:
                win += 1
        wins.append(win)
    
    return math.prod(wins)

def parse_two(inp):
    t, d = inp.split('\n')
    t = t.split()
    t = int(''.join(t[1:]))

    d = d.split()
    d = int(''.join(d[1:]))

    return t, d

def part_two(inp):
    t, d = parse_two(inp)

    win = 0
    for hold in range(t): 
        if (t-hold)*hold > d:
            lb = hold
            break
    for hold in range(t, 0, -1):
        if (t-hold)*hold > d:
            ub = hold
            break
    
    
    return ub-lb+1

# print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

print("Test Two:", part_two(test))

print("Part Two:", part_two(inp))
