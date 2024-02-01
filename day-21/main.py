import re
from collections import defaultdict

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


def ints(s):
    return list(map(int, re.findall(r'\d+', s)))


def arithmetic_sum(n, a, b, c):
    return a + n * (b - a + (n - 1) * (c - b - b + a) // 2)


def cmod(in_x, in_cols):
    return complex(in_x.real % in_cols, in_x.imag % in_cols)


data = open('../inputs/day21.txt').read().strip()
# data = open('sample').read().strip().splitlines()
lines = data.split('\n')
tmp = [[c for c in row] for row in lines]
rows, cols = len(tmp), len(tmp[0])

grid = {}
G = {}

start = None
for y, row in enumerate(lines):
    for x, col in enumerate(row):
        grid[(x, y)] = col
        if col == 'S':
            start = (x, y)
            print("Found point S at coordinates:", start)
        if col in '.S':
            G[y + x * 1j] = col
steps = 64
visited = defaultdict(set)
visited[0].add(start)

for s in range(steps):
    for point in visited[s]:
        x, y = point
        for tmp in DIRECTIONS:
            dx, dy = tmp
            ix, iy = x + dx, y + dy
            # print(x, dx, y, dy, ix, iy, grid.get((ix, iy), None))
            if grid.get((ix, iy), None) in ['.', 'S']:
                visited[s + 1].add((ix, iy))

print(len(visited.get(len(visited) - 1)))

to_visit = {x for x in G if G[x] == 'S'}

done = []
visited = []
for s in range(3 * cols):
    # if s == steps:
    #     print(len(to_visit))
    if s % cols == 65:
        visited.append(len(to_visit))
    to_visit = {p + d for d in {1, -1, 1j, -1j} for p in to_visit if cmod(p + d, cols) in G}

# part2
print(arithmetic_sum(26501365 // cols, visited[0], visited[1], visited[2]))
