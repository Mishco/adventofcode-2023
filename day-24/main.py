import re

import z3


def ints(s):
    return list(map(int, re.findall(r'\d+', s)))


with open("../inputs/day24.txt") as f:
    content = [x.strip() for x in f.readlines()]

hail = []
S = []
for stone in content:
    p, v = stone.split(' @ ')
    p = [int(x) for x in p.split(', ')]
    v = [int(x) for x in v.split(', ')]
    hail.append((p, v))
    S.append((p[0], p[1], p[2], v[0], v[1], v[2]))


def intersect(a, b):
    ap, av = a
    slope_a = av[1] / av[0]
    bp, bv = b
    slope_b = bv[1] / bv[0]
    if slope_b == slope_a:
        return False, -1, -1
    ayi = ap[1] - slope_a * ap[0]
    byi = bp[1] - slope_b * bp[0]
    x = (byi - ayi) / (slope_a - slope_b)
    y = slope_a * (byi - ayi) / (slope_a - slope_b) + ayi
    return True, x, y


intersections = {}
inside = 0
test = (200000000000000, 400000000000000)

for a, stone1 in enumerate(hail):
    for b, stone2 in enumerate(hail[a + 1:], start=a + 1):
        valid, x, y = intersect(stone1, stone2)
        if not valid:
            continue
        dx1 = x - stone1[0][0]
        dy1 = y - stone1[0][1]
        if (dx1 > 0) != (stone1[1][0] > 0) or (dy1 > 0) != (stone1[1][1] > 0):
            continue
        dx2 = x - stone2[0][0]
        dy2 = y - stone2[0][1]
        if (dx2 > 0) != (stone2[1][0] > 0) or (dy2 > 0) != (stone2[1][1] > 0):
            continue
        if test[0] <= x <= test[1] and test[0] <= y <= test[1]:
            inside += 1
        intersections[(a, b)] = test[0] <= x <= test[1] and test[0] <= y <= test[1]
# part1
print(inside)

x, y, z, vx, vy, vz = z3.Int('x'), z3.Int('y'), z3.Int('z'), z3.Int('vx'), z3.Int('vy'), z3.Int('vz')
n = len(S)

T = [z3.Int(f'T{i}') for i in range(n)]
solver = z3.Solver()

for i in range(n):
    solver.add(x + T[i] * vx - S[i][0] - T[i] * S[i][3] == 0)
    solver.add(y + T[i] * vy - S[i][1] - T[i] * S[i][4] == 0)
    solver.add(z + T[i] * vz - S[i][2] - T[i] * S[i][5] == 0)
res = solver.check()
mmm = solver.model()
# part2
print(mmm.eval(x + y + z))  # 557789988450159
