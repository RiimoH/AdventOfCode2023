from icecream import ic
from collections import OrderedDict, defaultdict
import re


test = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def hash(inp):
    cv = 0
    for char in inp:
        cv += ord(char)
        cv *= 17
        cv %= 256
    return cv


def parse(inp):
    ...


def part_one(inp):
    inp = "".join(inp.split("\n"))
    s = 0
    for i in inp.split(","):
        ic(i)
        s += ic(hash(i))

    return s


def part_two(inp):
    inp = "".join(inp.split("\n"))
    boxes = defaultdict(OrderedDict)
    for i in inp.split(","):
        label, operation, focal = ic(re.match(r"([a-z]+)([=-])([0-9]?)", i).groups())

        box = hash(label)

        if operation == "-":
            boxes[box].pop(label, None)
        elif operation == "=":
            boxes[box][label] = focal

    s = 0
    for bn, box in boxes.items():
        for sn, b in enumerate(box, 1):
            s += (int(bn) + 1) * sn * int(box[b])

    return s


with open("15.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test))

ic.disable()
print("Part One:", part_one(inp))

ic.enable()
print("Test Two:", part_two(test))

ic.disable()
print("Part Two:", part_two(inp), "> 50068")
