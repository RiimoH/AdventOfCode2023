from icecream import ic
from collections import defaultdict


test = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

test2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


class Module:
    def __init__(self, name=None, receiver=None):
        self.name = name
        self._receiver = receiver
        self._inputs = {}

    def pulse(self, sender, pulse):
        ...

    def add_input(self, origin, pulse=0):
        self._inputs[origin] = pulse


class BModule(Module):
    def pulse(self):
        return [(r, (self.name, 0)) for r in self._receiver]


class CModule(Module):
    def pulse(self, sender, pulse):
        self._inputs[sender] = pulse

        if all(self._inputs.values()):
            return [(r, (self.name, 0)) for r in self._receiver]
        else:
            return [(r, (self.name, 1)) for r in self._receiver]


class FFModule(Module):
    def __init__(self, name, receiver):
        super().__init__(name, receiver)
        self._state: bool = False

    def pulse(self, sender, pulse):
        if not pulse:
            self._state = not self._state
            return [(r, (self.name, int(self._state))) for r in self._receiver]


def parse(inp):
    modules = defaultdict(Module)

    for line in inp.splitlines():
        m, r = line.split(" -> ")
        if m == "broadcaster":
            modules[m] = BModule(m, r.split(", "))
        elif m.startswith("%"):
            modules[m[1:]] = FFModule(m[1:], r.split(", "))
        elif m.startswith("&"):
            modules[m[1:]] = CModule(m[1:], r.split(", "))

    for n, mod in modules.items():
        for r in mod._receiver:
            if r not in modules:
                continue
            else:
                modules[r].add_input(n)

    return modules


def part_one(inp, pushes=1):
    modules = parse(inp)
    low_pulses = 0
    high_pulses = 0

    for _ in range(pushes):
        low_pulses += 1
        pulses: list = modules["broadcaster"].pulse()

        calc = [int(x) for (_, (_, x)) in pulses]
        high_pulses += sum(calc)
        low_pulses += len(calc) - sum(calc)

        while pulses:
            (receiver, (sender, pulse)) = pulses.pop(0)
            ic(f"{sender} -{'high' if pulse else 'low'}-> {receiver}")
            new_pulses = modules[receiver].pulse(sender, pulse)

            if new_pulses:
                calc = [int(x) for (_, (_, x)) in new_pulses]

                high_pulses += sum(calc)
                low_pulses += len(calc) - sum(calc)

                pulses.extend(new_pulses)

    return low_pulses * high_pulses, low_pulses, high_pulses


def part_two(inp):
    modules = parse(inp)
    low_pulses = 0
    high_pulses = 0

    push = 0

    while True:
        push += 1
        low_pulses += 1
        pulses: list = modules["broadcaster"].pulse()

        calc = [int(x) for (_, (_, x)) in pulses]
        high_pulses += sum(calc)
        low_pulses += len(calc) - sum(calc)

        while pulses:
            (receiver, (sender, pulse)) = pulses.pop(0)
            if receiver == "rx" and pulse == 0:
                return push
            ic(f"{sender} -{'high' if pulse else 'low'}-> {receiver}")
            new_pulses = modules[receiver].pulse(sender, pulse)

            if new_pulses:
                calc = [int(x) for (_, (_, x)) in new_pulses]

                high_pulses += sum(calc)
                low_pulses += len(calc) - sum(calc)

                pulses.extend(new_pulses)

    return low_pulses * high_pulses, low_pulses, high_pulses


with open("20.inp") as fp:
    inp = fp.read()

ic.disable()
print("Test One:", part_one(test, 1_000))
print("Test One:", part_one(test2, 1_000))

print("Part One:", part_one(inp, 1_000))

# print("Test Two:", part_two(test))

print("Part Two:", part_two(inp))
