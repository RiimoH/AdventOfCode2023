from icecream import ic
from collections import defaultdict


test = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""


def parse(inp):
    inp = inp.splitlines()

    connections = defaultdict(list)

    for line in inp:
        x, con = line.split(": ")
        con = con.split(" ")
        connections[x].extend(con)
        for c in con:
            connections[c].append(x)

    return connections


def part_one(inp):
    connections = parse(inp)

    visited_one = set()
    barrier = {"jkn", "ljm", "gst"}
    queue = [
        "cfn",
    ]

    while queue:
        s = queue.pop()
        visited_one.add(s)
        queue.extend(
            [x for x in connections[s] if (x not in visited_one) and (x not in barrier)]
        )

    barrier = {"cfn", "sfd", "rph"}
    visited_two = set()
    queue = [
        "jkn",
    ]

    while queue:
        s = queue.pop()
        visited_two.add(s)
        queue.extend(
            [x for x in connections[s] if (x not in visited_two) and (x not in barrier)]
        )

    return len(visited_one) * len(visited_two)


def part_two(inp):
    ...


with open("25.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))

print("Part One:", part_one(inp))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
