# --- Day 18: Lavaduct Lagoon ---
#
# https://adventofcode.com/2023/day/18
#
# Shoelace_formula https://en.wikipedia.org/wiki/Shoelace_formula
# Pick's theorem https://en.wikipedia.org/wiki/Pick%27s_theorem

def collect_points(data):
    pos = (0, 0)
    points = [pos]
    perimeter = 0
    for item in data:
        direction, deep, colour = item.split()

        direction = DIRS[DNS.index(direction)]
        deep = int(deep)

        pos = (pos[0] + direction[0] * deep, pos[1] + direction[1] * deep)
        perimeter += deep
        points.append(pos)

    return points, perimeter


def collect_points_part2(data):
    pos = (0, 0)
    points = [pos]
    perimeter = 0
    for line in data:
        line = line.split("#")[1].split(")")[0]
        direction = DIRS[int(line[-1])]
        deep = int(line[:-1], 16)
        pos = (pos[0] + direction[0] * deep, pos[1] + direction[1] * deep)
        perimeter += deep
        points.append(pos)

    return points, perimeter


def calc(input_lines, part2=False):
    if part2:
        points, perimeter = collect_points_part2(input_lines)
    else:
        points, perimeter = collect_points(input_lines)
    points = points[::-1]
    count = 0
    for i in range(len(points) - 1):
        count += (points[i][1] + points[i + 1][1]) * (points[i][0] - points[i + 1][0])

    res = perimeter // 2 + count // 2 + 1
    return res


if __name__ == '__main__':
    lines = [x for x in open('../inputs/day18.txt').read().strip().split('\n')]
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    DNS = ['R', 'D', 'L', 'U']

    print("part1: ", calc(lines))
    print("part2: ", calc(lines, True))
