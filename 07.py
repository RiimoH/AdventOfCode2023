from icecream import ic
from collections import Counter, namedtuple

test = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def parse(inp):
    hands = []
    for line in inp.split("\n"):
        k, l = line.split()
        hands.append([k, int(l)])

    return hands


def part_one(inp):
    def evaluate(hand):
        c = Counter(hand[0])
        v = list(c.values())

        if 5 in v:
            hand.append(7)
        elif 4 in v:
            hand.append(6)
        elif 3 in v and 2 in v:
            hand.append(5)
        elif 3 in v and 2 not in v:
            hand.append(4)
        elif v.count(2) == 2:
            hand.append(3)
        elif v.count(2) == 1:
            hand.append(2)
        else:
            hand.append(1)

        values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }

        for c in hand[0]:
            hand.append(values[c])

        return hand

    hands = parse(inp)
    hands = list(map(evaluate, hands))

    hands.sort(key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))

    total = 0

    for i, h in enumerate(hands, start=1):
        total += i * h[1]

    return total


def part_two(inp):
    def evaluate(hand):
        c = Counter(hand[0])

        jokers = c["J"] or 0
        del c["J"]
        v = list(c.values())
        if not v:
            v.append(0)
        i = v.index(max(v))
        v[i] += jokers

        if 5 in v:
            hand.append(7)
        elif 4 in v:
            hand.append(6)
        elif 3 in v and 2 in v:
            hand.append(5)
        elif 3 in v and 2 not in v:
            hand.append(4)
        elif v.count(2) == 2:
            hand.append(3)
        elif v.count(2) == 1:
            hand.append(2)
        else:
            hand.append(1)

        values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 1,
            "Q": 12,
            "K": 13,
            "A": 14,
        }

        for c in hand[0]:
            hand.append(values[c])

        return hand

    hands = parse(inp)
    hands = list(map(evaluate, hands))

    hands.sort(key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))

    total = 0

    for i, h in enumerate(hands, start=1):
        total += i * h[1]

    return total


with open("07.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

print("Test Two:", part_two(test))

print("Part Two:", part_two(inp))
