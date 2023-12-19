from icecream import ic
from typing import Dict, List
import re
from collections import namedtuple

test = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

Part = namedtuple("Part", ["x", "m", "a", "s"])


def parse(inp):
    workflows = {}
    parts = []

    wf, p = inp.split("\n\n")

    for match in re.finditer(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)", p):
        parts.append(Part(*map(int, match.groups())))

    for w in wf.splitlines():
        name, rules = w.strip("}").split("{")
        rules = rules.split(",")
        last = rules[-1]
        rules = [
            re.match(r"([amsx])([<>])(\d+):(\w+)", rule).groups() for rule in rules[:-1]
        ]

        workflows[name] = {"rules": rules, "last": last}

    return workflows, parts


def part_one(inp):
    comp = {
        ">": lambda valr, valp: valp > valr,
        "<": lambda valr, valp: valp < valr,
    }

    def eval_rules(part, wf_rules, wf_last):
        while wf_rules:
            rule = wf_rules.pop(0)

            if comp[rule[1]](int(rule[2]), getattr(part, rule[0])):
                return rule[3]

        return wf_last

    workflows, parts = ic(parse(inp))

    accepted = []

    for part in parts:
        ic(part)
        result = eval_rules(part, workflows["in"]["rules"][:], workflows["in"]["last"])

        while result not in ["R", "A"]:
            ic(result)
            result = eval_rules(
                part, workflows[result]["rules"][:], workflows[result]["last"]
            )

        if result == "A":
            accepted.append(part)

    return sum(map(sum, accepted))


def part_two(inp):
    def eval_rules(part, wf_rules, wf_last):
        while wf_rules:
            rule = wf_rules.pop(0)

            l = int(rule[2])

            if l in part[rule[0]]:
                ypart = part.copy()
                ypart["n"] = rule[3]
                if rule[1] == "<":
                    ypart[rule[0]] = part[rule[0]][: part[rule[0]].index(l)]
                    part[rule[0]] = part[rule[0]][part[rule[0]].index(l) :]
                else:
                    ypart[rule[0]] = part[rule[0]][part[rule[0]].index(l) + 1 :]
                    part[rule[0]] = part[rule[0]][: part[rule[0]].index(l) + 1]
                yield ypart

        part["n"] = wf_last
        yield part

    get_poss = (
        lambda part: len(part["x"]) * len(part["m"]) * len(part["a"]) * len(part["s"])
    )

    workflows, _ = parse(inp)

    parts = [
        {
            "n": "in",
            "x": range(1, 4001),
            "m": range(1, 4001),
            "a": range(1, 4001),
            "s": range(1, 4001),
        },
    ]
    total = 0

    while parts:
        part = parts.pop()

        ic(part["n"], get_poss(part))

        result = eval_rules(
            part, workflows[part["n"]]["rules"][:], workflows[part["n"]]["last"]
        )

        for npart in result:
            if npart["n"] == "A":
                total += get_poss(npart)

            elif npart["n"] == "R":
                continue

            else:
                parts.append(npart)

    return total


with open("19.inp") as fp:
    inp = fp.read()

# print("Test One:", part_one(test))

# ic.disable()
# print("Part One:", part_one(inp), "> 284944")

print("Test Two:", part_two(test))

ic.disable()
print("Part Two:", part_two(inp))
