from icecream import ic
from collections import defaultdict
from functools import lru_cache

test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def parse(line):
    card, nums = line.split(":")
    _, cid = card.split()
    cid = int(cid)

    wn, cn = nums.split(" | ")

    win_nums = list(map(int, wn.split()))
    card_nums = list(map(int, cn.split()))

    return cid, win_nums, card_nums


def winning_points(win_nums, card_nums):
    score = 0
    for cn in card_nums:
        if cn in win_nums:
            score += score or 1

    return score


def part_one(inp):
    total_score = 0
    for line in inp.split("\n"):
        cid, win_nums, card_nums = parse(line)
        score = winning_points(win_nums, card_nums)
        total_score += score
        # print(f"Card {cid} scores {score} points.")

    return total_score


def part_two(inp):
    @lru_cache
    def try_card(cid):
        lcards = defaultdict(int)
        lcards[cid] += 1
        for ncid in cards[cid]["r"]:
            for c, v in try_card(ncid).items():
                lcards[c] += v

        return lcards

    cards = {}
    for line in inp.split("\n"):
        cid, win_nums, card_nums = parse(line)
        score = 0
        for cn in card_nums:
            if cn in win_nums:
                score += 1

        cards[cid] = {
            "wn": tuple(win_nums),
            "cn": tuple(card_nums),
            "n": 0,
            "r": [cid + 1 + i for i in range(0, score)],
        }

    for card in cards:
        for c, v in try_card(card).items():
            cards[c]["n"] += v

    total_cards = 0
    for cid, d in cards.items():
        total_cards += d["n"]

    return total_cards


print("Test One:", part_one(test))

with open("04.inp") as fp:
    inp = fp.read()

print("Part One:", part_one(inp))

print("Test Two:", part_two(test))

print("Part Two:", part_two(inp))
