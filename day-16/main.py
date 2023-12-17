# def read_grid_xy(infile):
#     g = []
#     w = 0
#     h = 0
#     for y, line in enumerate(infile):
#         line = line.strip()
#         g.append(line)
#         w = max(w, y+1)
#         h = max(h, len(line))
#         if len(line) == 0:
#             break
#     return (w, h, g)

# def v_add(p0, p1):
#     return tuple(map(lambda pair: pair[0] + pair[1], zip(p0, p1)))

# UP = (0, -1)
# DOWN = (0, 1)
# LEFT = (-1, 0)
# RIGHT = (1, 0)

# infile = open("../inputs/day16.txt")
# (w, h, grid) = read_grid_xy(infile)

# old_p = set()
# new_p = set([((0,0), RIGHT)])
# d = RIGHT
# while old_p != new_p:
#     old_p = new_p.copy()

#     adds = []
#     for pp in old_p:
#         p = pp[0]
#         d = pp[1]

#         c = grid[p[1]][p[0]]
#         if c == '.':
#             adds.append((v_add(p, d), d))
#         elif c == '|':
#             if d == RIGHT or d == LEFT:
#                 adds.append((v_add(p, UP), UP))
#                 adds.append((v_add(p, DOWN), DOWN))
#             if d == UP or d == DOWN:
#                 adds.append((v_add(p, d), d))
#         elif c == '-':
#             if d == UP or d == DOWN:
#                 adds.append((v_add(p, LEFT), LEFT))
#                 adds.append((v_add(p, RIGHT), RIGHT))
#             if d == RIGHT or d == LEFT:
#                 adds.append((v_add(p, d), d))
#         elif c == '\\':
#             if d == UP:
#                 d = LEFT
#             elif d == DOWN:
#                 d = RIGHT
#             elif d == RIGHT:
#                 d = DOWN
#             elif d == LEFT:
#                 d = UP
#             adds.append((v_add(p, d), d))
#         elif c == '/':
#             if d == UP:
#                 d = RIGHT
#             elif d == DOWN:
#                 d = LEFT
#             elif d == RIGHT:
#                 d = UP
#             elif d == LEFT:
#                 d = DOWN
#             adds.append((v_add(p, d), d))
#         else:
#             assert(False)

#     for p in adds:
#         if p[0][0] >= 0 and p[0][1] >= 0 and p[0][0] < w and p[0][1] < h:
#             new_p.add(p)


# print(len(set(map(lambda p: p[0], new_p))))


with open("../inputs/day16.txt") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}


def energized(entry, d):
    q = [(entry - d, d)]
    seen = set()
    while q:
        z, d = q.pop()
        if (z, d) in seen:
            continue
        seen.add((z, d))
        newz = z + d
        if newz not in board:
            continue
        match board[newz]:
            case "|" if d.imag:
                new_dir = [1, -1]
            case "-" if d.real:
                new_dir = [1j, -1j]
            case "/":
                new_dir = [(d * 1j).conjugate()]
            case "\\":
                new_dir = [(d * -1j).conjugate()]
            case _:
                new_dir = [d]
        q += [(newz, newd) for newd in new_dir]
    return len({x[0] for x in seen}) - 1

print(energized(0, 1j)) # Part 1, 7477

N, M = len(ls), len(ls[0])
entries = [(i, 1j) for i in range(N)]
entries += [(i + (M - 1) * 1j, -1j) for i in range(N)]
entries += [(i * 1j, 1) for i in range(M)]
entries += [(N - 1 + i * 1j, -1) for i in range(M)]
print(max(energized(*x) for x in entries)) # Part 2