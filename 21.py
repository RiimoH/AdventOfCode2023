from icecream import ic
from collections import deque

test = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


def parse(inp):
    board = {}
    for r, row in enumerate(inp.splitlines()):
        for c, char in enumerate(row):
            board[(r, c)] = char if char != "S" else "."
            if char == "S":
                s = (r, c)
    return board, s


dirs = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)


def part_one(inp, step_num=1):
    board, (sr, sc) = parse(inp)

    visited = {
        (0, sr, sc),  # 1 is odd, 0 is even
    }

    steps = [
        (sr, sc),
    ]

    for step in range(1, step_num + 1):
        even_odd = step % 2
        new_steps = list()
        for sr, sc in steps:
            for dr, dc in dirs:
                npos = sr + dr, sc + dc
                if board.get(npos, "#") == "#":
                    continue
                if (even_odd, *npos) not in visited and npos not in new_steps:
                    new_steps.append(npos)
                visited.add(
                    (even_odd, *npos),
                )
        steps = new_steps

        # l = [list(r) for r in inp.splitlines()]
        # for eo, r, c in visited:
        #     if eo == even_odd:
        #         l[r][c] = "O"
        # s = "\n".join(["".join(r) for r in l])
        # print(s)

    return len(list(filter(lambda x: x[0] == 0, visited)))


def multi_tile_bfs(grid, start: tuple[int, int], steps_available: int) -> int:
    """Modified BFS that now also includes a tile coordinate as part of state.
    Args:
        grid (_type_): 2D grid of chars
        start (tuple[int,int]): start location in the grid
        steps_available (int): steps available

    Returns int: count of valid locations to land on, when we've run out of steps
    """
    steps_remaining = steps_available
    current_tile = (0, 0)
    # (tile coordinate, location in tile, steps remaining)
    queue: deque[tuple[tuple[int, int], tuple[int, int], int]] = deque(
        [(current_tile, start, steps_remaining)]
    )

    seen = set()  # combination of (tile, location)
    answer: set[
        tuple[tuple, tuple]
    ] = set()  # the number of locations we can get to in the required number of steps

    side_len = len(grid)
    tiles_for_steps = (steps_available // side_len) + 1
    ic(f"{tiles_for_steps=}")

    while queue:
        # When we pop, we have already updated tile and location in the tile to be valid
        current_tile, current_locn, steps_remaining = queue.popleft()

        if steps_remaining >= 0:
            if (
                steps_remaining % 2 == 0
            ):  # we can always get back to this location in an even number of steps
                answer.add(
                    (current_tile, current_locn)
                )  # so this location will be possible in our target number of steps

            if steps_remaining > 0:  # get next possible location
                steps_remaining -= 1
                neighbours = [
                    (current_locn[0] + dx, current_locn[1] + dy) for dx, dy in (dirs)
                ]
                for (
                    neighbour
                ) in (
                    neighbours
                ):  # update current tile, and offset location in tile by tile width/height, as required
                    new_tile = current_tile
                    if neighbour[0] < 0:  # move to tile on the left
                        new_tile = (current_tile[0] - 1, current_tile[1])
                        neighbour = (neighbour[0] + side_len, neighbour[1])
                    if neighbour[0] >= side_len:  # move to tile on the right
                        new_tile = (current_tile[0] + 1, current_tile[1])
                        neighbour = (neighbour[0] - side_len, neighbour[1])
                    if neighbour[1] < 0:  # move to tile above
                        new_tile = (current_tile[0], current_tile[1] - 1)
                        neighbour = (neighbour[0], neighbour[1] + side_len)
                    if neighbour[1] >= side_len:  # move to tile below
                        new_tile = (current_tile[0], current_tile[1] + 1)
                        neighbour = (neighbour[0], neighbour[1] - side_len)

                    if (new_tile, neighbour) in seen or grid[neighbour[1]][
                        neighbour[0]
                    ] == "#":
                        continue  # do nothing

                    # With max distance of 327, this is 2.5 tiles. So 3 either side should be neough.
                    # -3, -2, -1, 0, 1, 2, 3 = 7x7
                    if (
                        abs(current_tile[0]) > tiles_for_steps
                        or abs(current_tile[1]) > tiles_for_steps
                    ):
                        ic(f"{new_tile=}")
                        assert False, "Not enough steps to move further out"

                    queue.append((new_tile, neighbour, steps_remaining))
                    seen.add((new_tile, neighbour))

    return len(answer)


def multi_tile_bfs(grid, start: tuple[int, int], steps_available: int) -> int:
    """Modified BFS that now also includes a tile coordinate as part of state.
    Args:
        grid (_type_): 2D grid of chars
        start (tuple[int,int]): start location in the grid
        steps_available (int): steps available

    Returns int: count of valid locations to land on, when we've run out of steps
    """
    steps_remaining = steps_available
    current_tile = (0, 0)
    # (tile coordinate, location in tile, steps remaining)
    queue: deque[tuple[tuple[int, int], tuple[int, int], int]] = deque(
        [(current_tile, start, steps_remaining)]
    )

    seen = set()  # combination of (tile, location)
    answer: set[
        tuple[tuple, tuple]
    ] = set()  # the number of locations we can get to in the required number of steps

    side_len = len(grid)
    tiles_for_steps = (steps_available // side_len) + 1
    ic(f"{tiles_for_steps=}")

    while queue:
        # When we pop, we have already updated tile and location in the tile to be valid
        current_tile, current_locn, steps_remaining = queue.popleft()

        if steps_remaining >= 0:
            if (
                steps_remaining % 2 == 0
            ):  # we can always get back to this location in an even number of steps
                answer.add(
                    (current_tile, current_locn)
                )  # so this location will be possible in our target number of steps

            if steps_remaining > 0:  # get next possible location
                steps_remaining -= 1
                neighbours = [
                    (current_locn[0] + dx, current_locn[1] + dy) for dx, dy in dirs
                ]
                for (
                    neighbour
                ) in (
                    neighbours
                ):  # update current tile, and offset location in tile by tile width/height, as required
                    new_tile = current_tile
                    if neighbour[0] < 0:  # move to tile on the left
                        new_tile = (current_tile[0] - 1, current_tile[1])
                        neighbour = (neighbour[0] + side_len, neighbour[1])
                    if neighbour[0] >= side_len:  # move to tile on the right
                        new_tile = (current_tile[0] + 1, current_tile[1])
                        neighbour = (neighbour[0] - side_len, neighbour[1])
                    if neighbour[1] < 0:  # move to tile above
                        new_tile = (current_tile[0], current_tile[1] - 1)
                        neighbour = (neighbour[0], neighbour[1] + side_len)
                    if neighbour[1] >= side_len:  # move to tile below
                        new_tile = (current_tile[0], current_tile[1] + 1)
                        neighbour = (neighbour[0], neighbour[1] - side_len)

                    if (new_tile, neighbour) in seen or grid[neighbour[1]][
                        neighbour[0]
                    ] == "#":
                        continue  # do nothing

                    # With max distance of 327, this is 2.5 tiles. So 3 either side should be neough.
                    # -3, -2, -1, 0, 1, 2, 3 = 7x7
                    if (
                        abs(current_tile[0]) > tiles_for_steps
                        or abs(current_tile[1]) > tiles_for_steps
                    ):
                        ic(f"{new_tile=}")
                        assert False, "Not enough steps to move further out"

                    queue.append((new_tile, neighbour, steps_remaining))
                    seen.add((new_tile, neighbour))

    return len(answer)


def reachable_plots(data, steps_available: int):
    grid = [[char for char in row] for row in data]
    grid_size = len(grid)

    ic(f"Grid width={grid_size}")
    assert grid_size == len(grid[0]), "The grid should be square"
    assert grid_size % 2 == 1, "The grid size is odd"

    (start,) = [
        (ri, ci)
        for ri, row in enumerate(grid)
        for ci, char in enumerate(row)
        if char == "S"
    ]

    assert start[0] == start[1] == grid_size // 2, "Start is in the middle"

    # For each location in the original grid (tile 0,0),
    # can we reach this same location in other tiles?
    answer = multi_tile_bfs(grid, start, steps_available)
    ic(f"We have {answer} final plots for {steps_available} steps.")

    return answer


def solve_quadratic(data, plot_counts: list[int], steps: int):
    """Return the total number of reachable plots in a specified number of steps,
    by calculating the answer to the quadratic formula.
    Here we calculate the coefficients a, b and c by using three sample values,
    obtained from a smaller grid.

    Args:
        data (_type_): The original grid tile.
        plot_counts (list[int]): The plot counts determined for small step counts.
        steps (int): The number of steps we must take.
    """
    grid = [[char for char in row] for row in data]
    grid_size = len(grid)

    # determine coefficients
    c = plot_counts[0]
    b = (4 * plot_counts[1] - 3 * plot_counts[0] - plot_counts[2]) // 2
    a = plot_counts[1] - plot_counts[0] - b

    x = (steps - grid_size // 2) // grid_size  # number of whole tile lengths
    return a * x**2 + b * x + c


with open("21.inp") as fp:
    inp = fp.read().splitlines()

# print("Test One:", part_one(test, step_num=6))
# print("Part One:", part_one(inp, step_num=64))

# print("Test Two:", part_two(test))

# print("Part Two:", part_two(inp))


step_counts = [6, 10, 20, 50, 100, 500]
sample_answers = [16, 50, 216, 1594, 6536, 167004]


for sample_step_count, sample_answer in zip(step_counts, sample_answers):
    reachable_plots(test.splitlines(), sample_step_count), sample_answer


step_counts = [
    64,
    65,
    196,
    327,
]  # 64 is just to check it matches what we had before
plot_counts = [
    (step_count, reachable_plots(inp, step_count)) for step_count in step_counts[1:]
]
plots = [
    (step_count, reachable_plots(inp, step_count)) for step_count in step_counts[1:]
]
ic(f"{plots=}")


ans = solve_quadratic(inp, plot_counts=[ct[1] for ct in plot_counts], steps=26501365)
ic(ans)
