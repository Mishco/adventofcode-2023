import re
from math import prod

import networkx as nx


def ints(s):
    return list(map(int, re.findall(r'\d+', s)))


if __name__ == '__main__':
    G = nx.Graph()

    data = open('../inputs/day25.txt').read().strip()
    # data = open('sample').read().strip() # should be 54

    lines = data.split('\n')

    for line in lines:
        v, adj = line.split(": ")
        for a in adj.strip().split(" "):
            G.add_edge(v, a)

    G.remove_edges_from(nx.minimum_edge_cut(G))
    result = prod([len(c) for c in nx.connected_components(G)])

    print("part1: ", result)  # 495607
