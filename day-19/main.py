import re


def ints(s):
    return list(map(int, re.findall(r'\d+', s)))


workflow, parts = open('../inputs/day19.txt').read().strip().split('\n\n')

parts = [ints(line) for line in parts.split("\n")]
workflow = {line.split("{")[0]: line.split("{")[1][:-1] for line in workflow.split("\n")}

print(f"{workflow=}")
print(f"{parts=}")


def process_part(part, current_workflow):
    w = workflow[current_workflow]
    items = w.split(',')
    # needs to be here because of eval function
    x, m, a, s = part
    for item in items:
        match item:
            case 'R':
                return False
            case 'A':
                return True

        if ':' not in item:
            return process_part(part, item)

        condition = item.split(':')[0]

        if eval(condition):
            match item.split(':')[1]:
                case 'R':
                    return False
                case 'A':
                    return True
            return process_part(part, item.split(':')[1])


def sort_parts(parts):
    total_rating = 0
    for part in parts:
        if process_part(part, 'in'):
            total_rating += sum(part)
    return total_rating


print("part1:", sort_parts(parts))


## part 2

def both(ch, gt, val, ranges):
    index = 'xmas'.index(ch)
    new_ranges = []

    for rng in ranges:
        lo, hi = rng[index]

        if gt:
            lo = max(lo, val + 1)
        else:
            hi = min(hi, val - 1)

        if lo <= hi:
            new_rng = list(rng)
            new_rng[index] = (lo, hi)
            new_ranges.append(tuple(new_rng))

    return new_ranges


def acceptance_ranges_outer(work):
    return acceptance_ranges_inner(workflow[work].split(","))


def acceptance_ranges_inner(w):
    item = w[0]
    match item:
        case 'R':
            return []
        case 'A':
            return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]

    if ":" not in item:
        return acceptance_ranges_outer(item)

    condition = item.split(":")[0]

    comparison_operator = ">" if ">" in condition else "<"
    character = condition[0]
    value = int(condition[2:])
    inverted_value = value + 1 if comparison_operator == ">" else value - 1

    true_ranges = both(character, comparison_operator == ">", value, acceptance_ranges_inner([item.split(":")[1]]))
    false_ranges = both(character, comparison_operator == "<", inverted_value, acceptance_ranges_inner(w[1:]))

    return true_ranges + false_ranges


p2 = 0
for rng in acceptance_ranges_outer('in'):
    v = 1
    for lo, hi in rng:
        v *= hi - lo + 1
    p2 += v

print(f"part2: {p2}")
