from icecream import ic
import re

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


def find_combinations(row, nums):
    if len(nums) == 1:
        if nums[0] > len(row):
            return 0
        else:
            return len(row) - nums[0] + 1

    if sum(nums) + len(nums) - 1 > len(row):  # there are not enough spaces to process
        return 0

    factors = []

    max_int = max(nums)
    if nums.count(max_int) == 1:
        row_lens = [len(x) for x in row]
        if row_lens.count(max_int) == 1:
            factors.append(
                find_combinations(
                    row[: row_lens.index(max_int)], nums[: nums.index(max_int)]
                )
            )
            factors.append(
                scd=find_combinations(
                    row[row_lens.index(max_int) + 1], nums[nums.index(max_int) + 1 :]
                )
            )

    for idx in range(len(row)):
        find_combinations(row[idx + len(nums[0]) :], nums[1:])


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
