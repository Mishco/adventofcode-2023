# data = open('../inputs/day15.txt').read().split(',')
# TODO: clean up
from collections import defaultdict

ll = open('../inputs/day15.txt').read().strip().split(',')
p1 = 0
p2 = 0


def hash(l):
    v = 0
    for ch in l:
        v += ord(ch)
        v *= 17
        v %= 256
    return v


lenses = [[] for i in range(256)]
lenslengths = [{} for i in range(256)]
for i, l in enumerate(ll):
    p1 += hash(l)
    label = l.split("=")[0].split("-")[0]
    v = hash(label)
    if "-" in l:
        if label in lenses[v]:
            lenses[v].remove(label)
    if "=" in l:
        if label not in lenses[v]:
            lenses[v].append(label)
        lenslengths[v][label] = int(l.split("=")[1])
for box, lns in enumerate(lenses):
    for i, lens in enumerate(lns):
        p2 += (box + 1) * (i + 1) * lenslengths[box][lens]
print(p1, p2)

def hash_(str):
  h = 0
  for c in str:
    h += ord(c)
    h = (17*h)%256
  return h

if __name__ == '__main__':

    data = open('../inputs/day15.txt').read().strip().split(',')

    print('part1: ', sum(hash_(d) for d in data))

    boxes = defaultdict(dict)

    for cmd in data:
        if '-' in cmd:
            label = cmd[:-1]
            h = hash_(label)
            boxes[hash_(label)].pop(label, None)
        else:
            label, i = cmd.split('=')
            boxes[hash_(label)][label] = int(i)

