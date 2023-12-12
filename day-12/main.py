from functools import lru_cache
from typing import Tuple

cache = {}

from functools import lru_cache
from typing import Tuple


@lru_cache
def count_ways(line: str, counts: tuple[int]) -> int:
    if not line:
        return 1 if not counts else 0

    if line.startswith("."):
        return count_ways(line.strip("."), counts)

    if line.startswith("?"):
        return (count_ways(line.replace("?", ".", 1), counts)
                + count_ways(line.replace("?", "#", 1), counts))

    if line.startswith("#"):
        if not counts or len(line) < counts[0] or any(c == "." for c in line[0:counts[0]]):
            return 0

        if len(counts) > 1:
            if len(line) < counts[0] + 1 or line[counts[0]] == "#":
                return 0

            return count_ways(line[counts[0] + 1:], counts[1:])

        return count_ways(line[counts[0]:], counts[1:])


def calculate_total(times: int) -> int:
    total = 0
    for ln in lines:
        row, numbers = ln.split()
        row = "?".join([row] * times)
        numbers: tuple[int, ...] = tuple([int(x) for x in numbers.split(',')] * times)
        total += count_ways(row, numbers)
    return total


if __name__ == '__main__':
    """
    For each row, count all of the different arrangements 
    of operational and broken springs that meet the given criteria. 
    What is the sum of those counts?
    """
    lines = open('../inputs/day12.txt', 'r').read().split('\n')

    times = 1  # part1
    total = 0

    # for ln in lines:
    #     row, nums = ln.split()
    #     row = "?".join([row] * times)
    #     nums = [int(n) for n in nums.split(",")] * times
    #     total += count_ways(row, nums)

    print(f"part1: {calculate_total(times=1)}")

    print(f"part2: {calculate_total(times=5)}")
    # for ln in lines:
    #     row, nums = ln.split()
    #     row = "?".join([row] * times)
    #     nums = [int(n) for n in nums.split(",")] * times
    #     total += count_ways(row, nums)

    # times = 5  # part2

    # print(get_total(5))

    # part2 - 18093821750095
