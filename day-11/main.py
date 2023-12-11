# --- Day 11: Cosmic Expansion ---
from itertools import combinations

import numpy as np

YEAR = 2023
DAY = 11
desc = '--- Day 11: Cosmic Expansion ---'
print(f"{desc}\nyear: {YEAR}\n")


def manhattan(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return abs(x2 - x1) + abs(y2 - y1)


def expand(factor, galaxies, cols, rows):
    expanded = []

    for (x, y) in galaxies:
        cs = (factor - 1) * sum(1 for c in cols if c < x)
        rs = (factor - 1) * sum(1 for r in rows if r < y)

        expanded.append((x + cs, y + rs))

    return expanded


def test():
    ln = open('sample').read().splitlines()

    galaxies, cols, rows = process_input(ln)
    t = sum(manhattan(g1, g2) for g1, g2 in combinations(expand(2, galaxies, cols, rows), 2))

    assert t == 374, 'should be 374'


def process_input(ln):
    w, h = len(ln), len(ln[0])
    g = [(x, y) for y in range(h) for x in range(w) if ln[y][x] == "#"]
    c = [x for x in range(w) if all(ln[y][x] == "." for y in range(h))]
    r = [y for y in range(h) if all(ln[y][x] == "." for x in range(w))]
    return g, c, r


def calculate(distance_mult=1) -> int:
    total = 0
    # distance_mult = 1  # part 1
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total += abs(galaxies[i][0] - galaxies[j][0]) + distance_mult * len(expand_rows[(min(
                galaxies[i][0], galaxies[j][0]) < expand_rows) & (max(galaxies[i][0], galaxies[j][0]) > expand_rows)])
            total += abs(galaxies[i][1] - galaxies[j][1]) + distance_mult * len(expand_cols[(min(
                galaxies[i][1], galaxies[j][1]) < expand_cols) & (max(galaxies[i][1], galaxies[j][1]) > expand_cols)])
    return total


if __name__ == '__main__':
    test()

    with open(f"../inputs/day{DAY}.txt", "r") as f:
        lines = [list(line.strip()) for line in f]

    # w, h = len(lines[0]), len(lines)
    #
    # galaxies = [(x, y) for y in range(h) for x in range(w) if lines[y][x] == "#"]
    # cols = [x for x in range(w) if all(lines[y][x] == "." for y in range(h))]
    # rows = [y for y in range(h) if all(lines[y][x] == "." for x in range(w))]

    galaxies, cols, rows = process_input(lines)

    part1 = sum(manhattan(g1, g2) for g1, g2 in combinations(expand(2, galaxies, cols, rows), 2))
    print(part1)  # 9522407

    part2 = sum(manhattan(g1, g2) for g1, g2 in combinations(expand(1000000, galaxies, cols, rows), 2))
    print(part2)

    # with numpy
    galaxy_input = open(f'../inputs/day{DAY}.txt').read()
    galaxy_map = np.array([list(line) for line in galaxy_input.split('\n')])
    expand_rows = np.array([])
    expand_cols = np.array([])
    for i in range(galaxy_map.shape[0]):
        if '#' in galaxy_map[i, :]:
            continue
        expand_rows = np.append(expand_rows, i)

    for j in range(galaxy_map.shape[1]):
        if '#' in galaxy_map[:, j]:
            continue
        expand_cols = np.append(expand_cols, j)

    galaxies = list(zip(*np.where(galaxy_map == '#')))

    total_distance = 0
    print(f"part1: {calculate(1)}")  # part1
    print(f"part2: {calculate(1000000 - 1)}")  # part2

    # print(f"part2: {total_distance}")  # 544723432977
    # 544723432977
