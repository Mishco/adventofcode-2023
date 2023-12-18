# https://en.wikipedia.org/wiki/Shoelace_formula
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


def calc(lines, part2=False):
    if part2:
        points, perimeter = collect_points_part2(lines)
    else:
        points, perimeter = collect_points(lines)
    points = points[::-1]
    count = 0
    for i in range(len(points) - 1):
        count += (points[i][1] + points[i + 1][1]) * (points[i][0] - points[i + 1][0])

    res = perimeter // 2 + count // 2 + 1
    return res


if __name__ == '__main__':
    # data = open('sample').read().strip().splitlines()
    # # grid = [[]]
    # grid = [['.' for _ in range(10)] for _ in range(10)]
    # x, y = 0, 0

    lines = [x for x in open('../inputs/day18.txt').read().strip().split('\n')]
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    DNS = ['R', 'D', 'L', 'U']

    pos = (0, 0)
    points = [pos]
    perimeter = 0

    print(calc(lines))
    print(calc(lines, True))

    # for item in lines:
    #     direction, deep, colour = item.split()
    #
    #     direction = DIRS[DNS.index(direction)]
    #     deep = int(deep)
    #
    #     pos = (pos[0] + direction[0] * deep, pos[1] + direction[1] * deep)
    #     perimeter += deep
    #     points.append(pos)
    #
    # points = points[::-1]
    # count = 0
    # for i in range(len(points) - 1):
    #     count += (points[i][1] + points[i + 1][1]) * (points[i][0] - points[i + 1][0])
    #
    # res = perimeter // 2 + count // 2 + 1
    # print("part1: ", res)
    #
    #
    # def run(part2):
    #     boundary = set()
    #     pos = (0, 0)
    #     points = [pos]
    #     perimeter = 0
    #     for line in lines:
    #         if part2:
    #             line = line.split("#")[1].split(")")[0]
    #             direction = DIRS[int(line[-1])]
    #             deep = int(line[:-1], 16)
    #         else:
    #             direction = DIRS[DNS.index(line.split(" ")[0])]
    #             deep = int(line.split(" ")[1])
    #         pos = (pos[0] + direction[0] * deep, pos[1] + direction[1] * deep)
    #         perimeter += deep
    #         points.append(pos)
    #
    #     points = points[::-1]
    #     a = 0
    #     for i in range(len(points) - 1):
    #         a += (points[i][1] + points[i + 1][1]) * (points[i][0] - points[i + 1][0])
    #     print(perimeter // 2 + a // 2 + 1)
    #
    #
    # run(False)  # part 1
    # run(True)  # part 2

    # # for item in data:
    # #     direction, deep, colour = item.split()
    # #     deep = int(deep)
    # #     for i in range(deep):
    # #         if direction == 'U':
    # #             grid[y - 1][x] = '#'  # colour
    # #         elif direction == 'D':
    # #             grid[y + 1][x] = '#'  # colour
    # #         elif direction == 'L':
    # #             grid[y][x - 1] = '#'  # colour
    # #         elif direction == 'R':
    # #             grid[y][x + 1] = '#'  # colour
    # #
    # #         # Update the current position
    # #         if direction == 'U':
    # #             y -= 1
    # #         elif direction == 'D':
    # #             y += 1
    # #         elif direction == 'L':
    # #             x -= 1
    # #         elif direction == 'R':
    # #             x += 1
    #
    # for row in grid:
    #     print(' '.join(row))
    #     # match direction:
    #     #     case 'U':
    #     #         # print('up')
    #     #         # grid[]
    #     #         y -= deep
    #     #     case 'D':
    #     #         # print('down')
    #     #         y += deep
    #     #     case 'L':
    #     #         # print('left')
    #     #         x -= deep
    #     #     case 'R':
    #     #         # print('right')
    #     #         x += deep
    #
    #     # grid[y][x] = '#' #colour
    #
    # # # Find the starting point for the flood fill
    # # start_x, start_y = None, None
    # # for y in range(len(grid)):
    # #     for x in range(len(grid[y])):
    # #         if grid[y][x] == '.':
    # #             start_x, start_y = x, y
    # #             break
    # #     if start_x is not None:
    # #         break
    # print()
    #     # Perform the flood fill
    # stack = [(0, 0)]
    # enclosed = [['.' for _ in range(10)] for _ in range(10)]
    # while stack:
    #     x, y = stack.pop()
    #     if grid[y][x] == '.':
    #         # grid[y][x] = '#'
    #         enclosed[y][x] = '#'
    #         if x > 0:
    #             stack.append((x - 1, y))
    #         if x < len(grid[y]) - 1:
    #             stack.append((x + 1, y))
    #         if y > 0:
    #             stack.append((x, y - 1))
    #         if y < len(grid) - 1:
    #             stack.append((x, y + 1))
    #
    # # Convert the grid to the enclosed area format
    # for y in range(len(grid)):
    #     for x in range(len(grid[y])):
    #         if enclosed[y][x] == '.':
    #             enclosed[y][x] = grid[y][x]
    #
    # for row in enclosed:
    #     print(' '.join(row))
    #
    # # volume = count * 1.0  # Each cell is 1 cubic meter
    # # print(f"The lagoon can hold {volume:.2f} cubic meters of lava.")
