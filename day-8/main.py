import math
import re

if __name__ == '__main__':

    test = """
    """
    # network = {
    #     "AAA": ("BBB", "BBB"),
    #     "BBB": ("AAA", "ZZZ"),
    #     "ZZZ": ("ZZZ", "ZZZ")
    # }

    # Running day Day 8: Haunted Wasteland:
    # 19783
    # 9177460370549

    # Start at node AAA
    current_node = "AAA"

    # Get the left/right instructions from the user
    lines = [i for i in open('../inputs/day08.txt', 'r').read().split('\n') if i.strip()]

    instructions = lines[0]
    network = {}
    for row in lines[1:]:
        # sample of line: `NFK = (LMH, RSS)`
        m = re.search("([A-Z0-9]+) = \\(([A-Z0-9]+), ([A-Z0-9]+)\\)", row)
        name, l, r = m.group(1), m.group(2), m.group(3)
        network[name] = (l, r)
    # print(network['NFK']) # ('LMH', 'RSS')

    res = []
    # starting point
    pos = ['AAA']
    for pos in pos:
        steps = 0
        while pos != 'ZZZ':
            if instructions[steps % len(instructions)] == 'L':
                pos = network[pos][0]
            else:
                pos = network[pos][1]
            steps += 1
        res.append(steps)

    print(f"part 1: {res[0]} ")

    res = []
    pos = [x for x in network if x.endswith("A")]
    for pos in pos:
        steps = 0
        while True:
            if instructions[steps % len(instructions)] == 'L':
                pos = network[pos][0]
            else:
                pos = network[pos][1]

            if pos.endswith('Z'):
                break
            steps += 1
        res.append(steps + 1)

    result = math.lcm(*res)
    print(f"part 2: {result}")
