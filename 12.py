from icecream import ic
import re
from functools import lru_cache
from typing import List

re_replace = r"\.+"

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
        rows.append((row, nums))

    return rows

@lru_cache
def brute(row: str, nums: List[int]):
    if len(nums) == 0:
        return 1

    s = 0

    s += brute('.'+row[1:], nums)
    num = nums[0]
    if row.startswith('#'*num) and row[num] != '#':
        s += brute(row[num+2:].lstrip('.'), nums[1:])

    return s

# @lru_cache
# def find_combinations(rows, nums):
#     if len(nums) == 1 or len(rows) == 1:

#         if nums[0] > max(map(len, rows)):
#             return 0
#         else:
#             return sum(len(row) - nums[0] + 1 for row in rows)

#     if sum(nums) + len(nums) - 1 > len(rows):  # there are not enough spaces to process
#         return 0

#     factors = []

#     max_int = max(nums)
#     if nums.count(max_int) == 1:
#         row_lens = [len(x) for x in rows]
#         if row_lens.count(max_int) == 1:
#             factors.append(
#                 find_combinations(
#                     rows[: row_lens.index(max_int)], nums[: nums.index(max_int)]
#                 )
#             )
#             factors.append(
#                 scd=find_combinations(
#                     rows[row_lens.index(max_int) + 1], nums[nums.index(max_int) + 1 :]
#                 )
#             )

#     for idx in range(len(rows)):
#         find_combinations(rows[idx + len(nums[0]) :], nums[1:])


def part_one(inp):
    rows = ic(parse(inp))

    for row, nums in rows:
        row = re.sub(re_replace, ".", row, re.MULTILINE)
        row = row.strip(".").rstrip(".")
        row = row.split(".")
        for i, seq in enumerate(row):
            if "?" not in seq:
                row[i] = len(seq)

        lint = max(nums)
        lint_first_idx = nums.index(lint)


def part_two(inp):
    ...


# with open("") as fp:
#     inp = fp.read()

print("Test One:", part_one(test))

# print("Part One:", part_one(inp))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))
