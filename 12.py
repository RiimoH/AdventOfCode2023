from icecream import ic
import functools
from typing import List, Tuple


test = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def parse(inp):
    rows = []

    for line in inp.split("\n"):
        row, nums = line.split()
        nums = [int(x) for x in nums.split(",")]
        rows.append((row, tuple(nums)))

    return rows


@functools.cache
def calc(row: str, groups: Tuple[int]) -> int:
    """Recursevly calculates all the possible combinations for a certain row and groups combination.

    Args:
        row (str): Any combination of '.#?'
        groups (Tuple[int]): All the groups that have to fit and not touch.

    Returns:
        int: Number of possible combinations
    """

    if not groups:
        if "#" not in row:
            return 1
        else:
            return 0

    if not row:
        return 0

    next_char = row[0]

    if next_char == ".":
        return dot(row, groups)

    elif next_char == "#":
        return pound(row, groups)

    else:
        return dot(row, groups) + pound(row, groups)


def dot(row, groups):
    return calc(row[1:], groups)


def pound(row, groups):
    next_group = groups[0]

    if len(row) == next_group:
        if "." not in row and len(groups) == 1:
            return 1
        else:
            return 0

    if len(row) < next_group:
        return 0

    if (
        row[:next_group].replace("?", "#") == next_group * "#"
        and row[next_group] in "?."
    ):
        return calc(row[next_group + 1 :], groups[1:])

    return 0


def part_one(inp):
    total = 0
    for row, groups in parse(inp):
        total += ic(calc(row, groups))

    return total


def part_two(inp):
    total = 0
    for row, groups in parse(inp):
        row = "?".join([row] * 5)
        groups = groups * 5

        total += calc(row, groups)

    return total


with open("12.inp") as fp:
    inp = fp.read()

print("Test One:", part_one(test))

ic.disable()
print("Part One:", part_one(inp))

print("Test Two:", part_two(test))

print("Part Two:", part_two(inp))


# @functools.cache
# def brute(record: str, groups: Tuple[int]):
#     if not groups:
#         if "#" not in record:
#             return 1
#         else:
#             return 0

#     if not record:
#         return 0

#     record = record.lstrip('.')

#     if len(groups) == 1:
#         return sum(record.startswith(groups[0], i) for i, _ in enumerate(record))

#     if record[0] == '#':
#         next_group = groups[0]

#         if "." in record[:next_group] or "#" in record[next_group]:
#             return 0

#         return brute(record[next_group+1:], groups[1:])

#     else: # record is '?'
#         # if ? is .


#     s = 0

#     s += brute(record[1:], groups)
#     num = groups[0]

#     take, go_on = record[:num], record[num:]
#     if "." not in take and (go_on.startswith(".") or go_on.startswith("?")):
#         s += brute(record[num + 1 :].lstrip("."), groups[1:])

#     return s


# def find_combinations(rows: List[str], nums: List[int]):
#     if len(nums) == 0:
#         return 1

#     max_int: int = max(nums)
#     if nums.count(max_int) == 1:
#         factors: List[int] = []
#         section_lengths = [len(x) for x in rows]

#         if section_lengths.count(max_int) == 1:
#             factors.append(
#                 find_combinations(
#                     rows[: section_lengths.index(max_int)], nums[: nums.index(max_int)]
#                 )
#             )
#             factors.append(
#                 find_combinations(
#                     rows[section_lengths.index(max_int) + 1 :],
#                     nums[nums.index(max_int) + 1 :],
#                 )
#             )
#         return prod(factors)

#     return brute(".".join(rows), tuple(nums))


# def part_one(inp):
#     rows = parse(inp)
#     s = 0
#     for row, nums in rows:
#         row = re.sub(r"\.+", ".", row, re.MULTILINE)
#         row = row.strip(".").rstrip(".")
#         row = row.split(".")

#         nrow = []
#         for i, seq in enumerate(row):
#             if "?" not in seq and nums.count(len(seq)) == 1:
#                 nums.remove(len(seq))
#             else:
#                 nrow.append(seq)

#         s += ic(find_combinations(nrow, tuple(nums)))

#     return s
