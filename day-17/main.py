from heapq import heappop, heappush

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

HUGE_NUMBER = float('inf')


def is_valid_pos(pos, arr):
    return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))


def run(min_distance, max_consecutive):
    q = [(0, 0, 0, -1)]
    visited = set()
    costs = {}
    while q:
        cost, x, y, disallowed_direction = heappop(q)

        if x == len(city_grid) - 1 and y == len(city_grid[0]) - 1:  # goal x, goal y
            return cost

        if (x, y, disallowed_direction) in visited:
            continue

        visited.add((x, y, disallowed_direction))

        for direction in range(4):
            if direction == disallowed_direction or (direction + 2) % 4 == disallowed_direction:
                continue

            cost_increase = 0

            for distance in range(1, max_consecutive + 1):
                xx = x + DIRECTIONS[direction][0] * distance
                yy = y + DIRECTIONS[direction][1] * distance

                if not is_valid_pos((xx, yy), city_grid):
                    break

                cost_increase += city_grid[xx][yy]
                if distance >= min_distance:
                    nc = cost + cost_increase

                    if costs.get((xx, yy, direction), HUGE_NUMBER) > nc:
                        costs[(xx, yy, direction)] = nc
                        heappush(q, (nc, xx, yy, direction))


if __name__ == '__main__':
    # data = open('sample').read().strip()
    data = open('../inputs/day17.txt').read().strip()

    # city_grid = [[int(y) for y in x] for x in open('../inputs/day17.txt').read().strip().split('\n')]
    L = data.split('\n')
    city_grid = [[int(c) for c in row] for row in L]

    start = (0, 0)
    # dest = (12, 12)
    rows = len(city_grid)
    cols = len(city_grid[0])

    print("part1: ", run(1, 3))
    print("part2: ", run(4, 10))
