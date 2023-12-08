from math import gcd
from icecream import ic
from collections import namedtuple
from itertools import cycle

test = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""


test2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

test3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

Node = namedtuple("Node", ["name", "left", "right"])


def parse(inp):
    instr, strnodes = inp.split("\n\n")
    nodes = {}
    for cn in strnodes.split("\n"):
        n, lr = cn.split(" = ")
        l, r = lr.strip("()").split(", ")
        nodes[n] = Node(n, l, r)

    return instr, nodes


def part_one(inp):
    instr, nodes = parse(inp)

    node = nodes["AAA"]
    count = 1
    for i in cycle(instr):
        if i == "L":
            node = nodes[node.left]
        else:
            node = nodes[node.right]

        if node.name == "ZZZ":
            return count
        else:
            count += 1


def part_two(inp):
    instr, nodes = parse(inp)
    running_nodes = [node for name, node in nodes.items() if name.endswith("A")]

    counts = []

    for node in running_nodes:
        count = 1
        for i in cycle(instr):
            if i == "L":
                node = nodes[node.left]
            else:
                node = nodes[node.right]

            if node.name.endswith("Z"):
                counts.append(count)
                break
            else:
                count += 1

    lcm = 1
    for i in counts:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


with open("08.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))
# print("Test One.2:", part_one(test2))

# print("Part One:", part_one(inp))

print("Test Two:", part_two(test3))

print("Part Two:", part_two(inp))
