import re
from collections.abc import Iterator

# 1444 nope
# 1446 nope

directions = {
    '>': [(1, 0)],
    '<': [(-1, 0)],
    '^': [(0, -1)],
    'v': [(0, 1)],
    '.': [(1, 0), (-1, 0), (0, 1), (0, -1)],
}

Pos = tuple[int, int]


def ints(s):
    return list(map(int, re.findall(r'\d+', s)))


data = open('../inputs/day23.txt').read().strip().splitlines()


# data = open('sample').read().strip().splitlines()
# print(data)


def get_neighbors(position: Pos,
                  trail_map: list[str],
                  slopes: bool = True) -> Iterator[Pos]:
    width = len(trail_map[0])
    height = len(trail_map)
    x, y = position

    for dx, dy in directions[trail_map[y][x] if slopes else '.']:
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < width and 0 <= new_y < height and trail_map[new_y][new_x] != '#':
            yield new_x, new_y


def is_dead_end(position: Pos, prev: Pos, neighbors: list[Pos], trail_map: list[str]) -> bool:
    if neighbors == [prev] and trail_map[position[1]][position[0]] in '<>^v':
        return True

    return False


def get_graph(trail_map: list[str],
              slopes: bool = True) -> dict[Pos, list[tuple[Pos, int]]]:
    vertices = [(1, 0)]
    visited = set()
    res_graph = {}
    while vertices:
        vertex = vertices.pop()
        if vertex in visited:
            continue
        res_graph[vertex] = []
        for next_step in get_neighbors(vertex, trail_map, slopes):
            length = 1
            prev = vertex
            position = next_step
            dead_end = False
            while True:
                neighbors = list(get_neighbors(position, trail_map, slopes))

                if is_dead_end(position, prev, neighbors, trail_map):
                    dead_end = True
                    break

                if len(neighbors) != 2:
                    break

                for neighbor in neighbors:
                    if neighbor != prev:
                        length += 1
                        prev = position
                        position = neighbor
                        break
            if dead_end:
                continue
            res_graph[vertex].append((position, length))
            vertices.append(position)
        visited.add(vertex)
    return res_graph


def iter_hike_lengths(in_graph: dict[Pos, list[tuple[Pos, int]]],
                      in_goal: Pos) -> Iterator[int]:
    start = (1, 0)
    stack = [(start, 0, {start})]

    while stack:
        last, length, visited = stack.pop()

        if last == in_goal:
            yield length
            continue

        for new, edge_length in in_graph[last]:
            if new in visited:
                continue
            stack.append((new, length + edge_length, visited | {new}))


goal = len(data[0]) - 2, len(data) - 1
# part1
graph = get_graph(data)
print(max(iter_hike_lengths(graph, goal)))

graph = get_graph(data, slopes=False)
# part2, (run cca 1 minute)
print(max(iter_hike_lengths(graph, goal)))

