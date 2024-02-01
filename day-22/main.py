import re


# 1444 nope
# 1446 nope

def ints(s):
    return list(map(int, re.findall(r'\d+', s)))


data = open('../inputs/day22.txt').read().strip().splitlines()
# data = open('sample').read().strip().splitlines()
print(data)

L = [c.split('~') for c in data]
print(L)


class Brick:
    def __init__(self, a: tuple, b: tuple):
        self.x = (min(a[0], b[0]), max(a[0], b[0]))
        self.y = (min(a[1], b[1]), max(a[1], b[1]))
        self.z = (min(a[2], b[2]), max(a[2], b[2]))

        self.below_list = set()
        self.above_list = set()

    def is_below(self, other):
        return (
                (self.x[0] <= other.x[1] and other.x[0] <= self.x[1])
                and (self.y[0] <= other.y[1] and other.y[0] <= self.y[1])
                and (self.z[1] <= other.z[0])
        )

    def drop(self, newz: int):
        len = self.z[1] - self.z[0]
        self.z = (newz, newz + len)

    def collapse(self):
        removed = {self}
        for other in self.above_list:
            other.check_collapse(removed)
        removed.remove(self)
        return removed

    def check_collapse(self, removed):
        if self.below_list.issubset(removed):
            removed.add(self)
            for other in self.above_list:
                other.check_collapse(removed)


bricks = []
for line in data:
    if line:
        start, end = line.split('~')
        start = tuple(map(int, start.split(',')))
        end = tuple(map(int, end.split(',')))
        bricks.append(Brick(start, end))

bricks.sort(key=lambda bbb: bbb.z[0])
by_zval = [[] for _ in range(bricks[-1].z[0])]
base = Brick((0, 0, 0), (1000, 1000, 0))
settled = [base]

for brick in bricks:
    top_z = max((other.z[1] for other in settled if other.is_below(brick)))
    brick.drop(top_z + 1)
    settled.append(brick)
    by_zval[top_z + 1].append(brick)

for brick in bricks:
    for other in by_zval[brick.z[1] + 1]:
        if brick.is_below(other):
            other.below_list.add(brick)
            brick.above_list.add(other)

remove_count = 0
chain_count = 0
for brick in bricks:
    if len(brick.above_list) == 0 or all(len(other.below_list) > 1 for other in brick.above_list):
        remove_count += 1
    else:
        supported = brick.collapse()
        chain_count += len(supported)

print(f"Part 1: {remove_count}")
print(f"Part 2: {chain_count}")
