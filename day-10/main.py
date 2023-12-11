### --- Day 10: Pipe Maze ---
import heapq
import networkx as nx

# Find the single giant loop starting at S.
# How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?
def get_neighbors(tile):
    neighbors = []
    row, col = tile
    if col+1 < len(pipe_system[row]) and pipe_system[row][col+1] == '-':
        neighbors.append((row, col+3))
    if row+1 < len(pipe_system) and pipe_system[row+1][col] == '|':
        neighbors.append((row+2, col))
    if col-1 >= 0 and pipe_system[row][col-1] == '-':
        neighbors.append((row, col-3))
    if row-1 >= 0 and pipe_system[row-1][col] == '|':
        neighbors.append((row-2, col))
    return neighbors if neighbors else []


# def dijkstra(start, end):
#     # Initialize the distance and visited dictionaries
#     distance = {start: 0}
#     visited = {}
#
#     # Initialize the priority queue with the starting tile
#     pq = [(0, start)]
#
#     # Loop until we've visited all tiles or found the end tile
#     while pq:
#         # Get the tile with the smallest distance from the priority queue
#         dist, tile = heapq.heappop(pq)
#
#         # If we've already visited this tile, skip it
#         if tile in visited:
#             continue
#
#         # Mark the tile as visited and update its distance
#         visited[tile] = True
#         distance[tile] = dist
#
#         # If we've reached the end tile, we're done
#         if tile == end:
#             break
#
#         # Add the neighbors of the current tile to the priority queue
#         for neighbor in get_neighbors(tile):
#             if neighbor not in visited:
#                 heapq.heappush(pq, (dist + 1, neighbor))
#
#     # Return the distance to the end tile
#     return distance.get(end, -1)

from collections import deque

def find_path(grid, start, end):
    queue = deque([start])
    visited = set([start])
    path = {start: None}

    while queue:
        curr_pos = queue.popleft()

        if curr_pos == end:
            return construct_path(path, start, end)

        for neighbor in get_neighbors(grid, curr_pos):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path[neighbor] = curr_pos

    return "No path found"

def get_neighbors(grid, pos):
    row, col = pos
    neighbors = []

    if row > 0 and grid[row-1][col] in "|FL":
        neighbors.append((row-1, col))
    if row < len(grid)-1 and grid[row+1][col] in "|FJ":
        neighbors.append((row+1, col))
    if col > 0 and grid[row][col-1] in "-FJ":
        neighbors.append((row, col-1))
    if col < len(grid[0])-1 and grid[row][col+1] in "-FL":
        neighbors.append((row, col+1))

    return neighbors

def construct_path(path, start, end):
    curr_pos = end
    path_taken = []

    while curr_pos != start:
        path_taken.append(curr_pos)
        curr_pos = path[curr_pos]

    path_taken.append(start)
    path_taken.reverse()

    return path_taken


if __name__ == '__main__':
    ttt = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

    # lines  = ttt.splitlines()
    # print(lines)
    # with open('input.txt', 'r') as f:
    #     pipe_system = [line.strip() for line in f]
    lines = [s for s in open('../inputs/day10.txt', 'r').read().split('\n') if s.strip()]
    print(lines)
    # l = [[int(i) for i in s.split()] for s in open('input').read().split('\n') if s.strip()]

    pipe_system=lines
    # Find the farthest point from the starting position
    farthest_point = max([int(c) for row in pipe_system for c in row if c.isdigit()])

    # start_point = [(row,row.index(c))  ]
    idx=0
    for row in pipe_system:
        for c in row:
            if c == 'S':
                start_point=(idx, row.index(c))
        idx+=1

    height = len(pipe_system)
    width = len(pipe_system[0])


    ax = -1
    ay = -1
    for i in range(height):
        for j in range(width):
            if "S" in pipe_system[i]:
                ax = i
                ay = pipe_system[i].find("S")
    print(ax, ay)

    # N, M = len(data), len(data[0])
    G = nx.Graph()
    data = pipe_system
    for x, line in list(enumerate(data)):
        for y, char in list(enumerate(line)):
            # North neighbour
            if x > 0 and data[x - 1][y] in "|7FS" and char in "|LJS":
                G.add_edge((x, y), (x - 1, y))
            # East neighbour
            if y < width - 1 and data[x][y + 1] in "-J7S" and char in "-LFS":
                G.add_edge((x, y), (x, y + 1))
            if char == "S":
                start = (x, y)

    cycle = nx.find_cycle(G, start)
    print("Part 1:", len(cycle) // 2)

    path_nodes = set(p[0] for p in cycle)
    visited = set()

    G2 = nx.grid_graph((height, width))
    G2.remove_nodes_from(path_nodes)

    for (x, y), (i, j) in cycle:
        # add nodes that are to the right side of a path
        dx, dy = i - x, j - y
        for i in (0, 1):
            node = x + i * dx - dy, y + i * dy + dx
            if node not in visited and node not in path_nodes:
                visited |= nx.node_connected_component(G2, node)

    print("Part 2:", len(visited))

    # break

    # Follow the loop and add up the distances
    steps = 0
    # rightward downward leftward upward
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    happy = ["-7J", "|LJ", "-FL", "|F7"]
    Sdirs = []
    for i in range(4):
        pos = dirs[i]
        bx = ax + pos[0]
        by = ay + pos[1]
        if 0 <= bx <= height and 0 <= by <= width and pipe_system[bx][by] in happy[i]:
            Sdirs.append(i)
    print(Sdirs)
    Svalid = 3 in Sdirs  # part 2

    # rightward downward leftward upward
    transform = {
        (0, "-"): 0,
        (0, "7"): 1,
        (0, "J"): 3,
        (2, "-"): 2,
        (2, "F"): 1,
        (2, "L"): 3,
        (1, "|"): 1,
        (1, "L"): 0,
        (1, "J"): 2,
        (3, "|"): 3,
        (3, "F"): 0,
        (3, "7"): 2,
    }

    curdir = Sdirs[0]
    cx = ax + dirs[curdir][0]
    cy = ay + dirs[curdir][1]
    ln = 1
    # O[ax][ay] = 1  # Part 2
    # while (cx, cy) != (ax, ay):
    #     O[cx][cy] = 1  # Part 2
    #     ln += 1
    #     curdir = transform[(curdir, G[cx][cy])]
    #     cx = cx + dirs[curdir][0]
    #     cy = cy + dirs[curdir][1]
    # print(ln)
    # print(ln // 2)

    # farthest_point = max([int(c) for row in pipe_system for c in row if c.isdigit()])

    # start = start_point #(2, 0)  # position of S
    # end = farthest_point #(3, 4)  # position of the end point

    # path = find_path(pipe_system, start, end)
    # print(path)


    # Compute the shortest path from the starting position to the farthest point
    # start_tile = start_point #(1, 1)
    # farthest_tile = [(row, col) for row in range(len(pipe_system)) for col in range(len(pipe_system[row])) if
    #                  pipe_system[row][col].isdigit() and int(pipe_system[row][col]) == farthest_point][0]
    # # shortest_path = dijkstra(start_tile, farthest_tile)
    #
    # # Print the result
    # # print(shortest_path)
    #
    #
    # # Define a function to get the neighbors of a tile
    # # Build the graph
    # graph = {}
    # for row in range(len(pipe_system)):
    #     for col in range(len(pipe_system[row])):
    #         if pipe_system[row][col] == '.':
    #             continue
    #         tile = (row, col)
    #         if tile not in graph:
    #             graph[tile] = []
    #         for neighbor in get_neighbors(tile):
    #             if neighbor in graph:
    #                 graph[tile].append(neighbor)
    #                 graph[neighbor].append(tile)

    # Find the tile that is farthest from the starting position along the loop
    # allow importing from parent folder
    # import sys
    #
    # sys.path.append('../AOC-2023')

    # util imports
    # from utils.readfile import *
    # from utils.calc import *
    # from utils.graph import *
    # from utils.util import *
    # # lib imports
    import re
    import math
    import copy
    import numpy as np
    from itertools import combinations, permutations, product
    import time

    start_time = time.time()

    # input parsing
    # def read_grid_2d(day):
        # with open(f"{day}/{day}.txt") as f:
        #     return [list(line.strip()) for line in f.readlines()]

    # lines = read_grid_2d('10')

    start = (29, 21)  # x, y

    # part 1
    print("PART 1:")
    ans = 1

    poly = [start]

    position = [start[0], start[1] - 1]
    last_move = [0, -1]
    while lines[position[1]][position[0]] != 'S':
        poly.append([*position])
        tile = lines[position[1]][position[0]]
        if tile == "|":
            if last_move == [0, 1]:
                position[1] += 1
            elif last_move == [0, -1]:
                position[1] -= 1
        elif tile == "-":
            if last_move == [1, 0]:
                position[0] += 1
            elif last_move == [-1, 0]:
                position[0] -= 1
        elif tile == "7":
            if last_move == [1, 0]:
                position[1] += 1
                last_move = [0, 1]
            elif last_move == [0, -1]:
                position[0] -= 1
                last_move = [-1, 0]
        elif tile == "J":
            if last_move == [1, 0]:
                position[1] -= 1
                last_move = [0, -1]
            elif last_move == [0, 1]:
                position[0] -= 1
                last_move = [-1, 0]
        elif tile == "L":
            if last_move == [-1, 0]:
                position[1] -= 1
                last_move = [0, -1]
            elif last_move == [0, 1]:
                position[0] += 1
                last_move = [1, 0]
        elif tile == "F":
            if last_move == [-1, 0]:
                position[1] += 1
                last_move = [0, 1]
            elif last_move == [0, -1]:
                position[0] += 1
                last_move = [1, 0]
        else:
            print("ERROR")
            break

        ans += 1

    print(ans // 2)

    # part 2
    print("PART 2:")
    print(poly)
    ans_2 = 0

    from matplotlib.path import Path

    p = Path(poly)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if [x, y] in poly:
                continue
            if p.contains_point((x, y)):
                ans_2 += 1

    print(ans_2)

    print("took %s seconds" % (time.time() - start_time))

        # print(current_tile)
    # Print the result
    print(steps)

    ####
    # this queue is synchronized, which is pretty pointless...
    with open("../inputs/day10-real.txt", "r") as f:
        m = [l.strip() for l in f]

        n = {
            "|": [(0, -1), (0, 1)],
            "-": [(-1, 0), (1, 0)],
            "L": [(0, -1), (1, 0)],
            "J": [(0, -1), (-1, 0)],
            "7": [(-1, 0), (0, 1)],
            "F": [(1, 0), (0, 1)],
        }

        x, y = None, None

        for yi, line in enumerate(m):
            for xi, c in enumerate(line):
                if c == "S":
                    x, y = xi, yi
                    break

        assert (x != None)
        assert (y != None)

        q = Queue()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            c = m[y + dy][x + dx]
            if c in n:
                for dx2, dy2 in n[c]:
                    if x == x + dx + dx2 and y == y + dy + dy2:
                        q.put((1, (x + dx, y + dy)))

        dists = {(x, y): 0}
        assert (q.qsize() == 2)

        while not q.empty():
            d, (x, y) = q.get()

            if (x, y) in dists:
                continue

            # print(d,(x,y))
            dists[(x, y)] = d

            for dx, dy in n[m[y][x]]:
                q.put((d + 1, (x + dx, y + dy)))

        print(f"Part 1: {max(dists.values())}")

        w = len(m[0])
        h = len(m)

        inside_count = 0
        for y, line in enumerate(m):
            for x, c in enumerate(line):
                if (x, y) in dists:
                    continue

                crosses = 0
                x2, y2 = x, y

                while x2 < w and y2 < h:
                    c2 = m[y2][x2]
                    if (x2, y2) in dists and c2 != "L" and c2 != "7":
                        crosses += 1
                    x2 += 1
                    y2 += 1

                if crosses % 2 == 1:
                    inside_count += 1

        print(f"Part 2: {inside_count}")