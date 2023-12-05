import re

test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

"""

location_numbers = []


def ints(s: str) -> list[int]:
    """

    :param s: (str): The input string to search for integers.
    :return: List[int]: A list of integers found in the input string.
    """
    """
    Return a list of integers found in the input string.

    Example:
    >>> ints("seeds: 3640772818 104094365 1236480411 161072229 376099792")
    [3640772818, 104094365, 1236480411, 161072229, 376099792]
    """
    return [int(m) for m in re.findall(r'-?[\d]+', s)]


data = open('../inputs/day05.txt', 'r').read()
parts = data.split('\n\n')
seed_names, map_sets = parts[0], parts[1:]
seeds = ints(parts[0])
min_location = 2 ** 63 - 1  # max int val

for seed in seeds:
    location = seed
    for map_set in map_sets:
        for line in map_set.split('\n')[1:]:
            dst_start, src_start, rng = ints(line)
            if location in range(src_start, src_start + rng):
                location = dst_start + (location - src_start)
                break
    min_location = min(min_location, location)

print(f"{min_location=}")
# first part 214922730

content = [line.strip() for line in data.splitlines()]
currents = []
nexts = ints(content[0])
unmapped = []

cleaned_content = content[2:]
cleaned_content = [i for i in cleaned_content if i != '']

for line in cleaned_content:
    numbers = ints(line)
    if not numbers:
        currents = nexts
        currents.extend(unmapped)
        nexts, unmapped = [], []
    else:
        currents.extend(unmapped)
        unmapped = []
        current_destination, current_source, range_map = numbers[:3]

        while len(currents) > 0:
            if currents[0] < current_source + range_map and currents[0] + currents[1] > current_source:
                to_map_start = max(currents[0], current_source)
                to_map_end = min(current_source + range_map, currents[0] + currents[1])
                to_map_range = to_map_end - to_map_start

                mapped_start = current_destination + (to_map_start - current_source)
                mapped_range = to_map_range
                nexts.append(mapped_start)
                nexts.append(mapped_range)

                if currents and currents[0] < to_map_start:
                    left_start = currents[0]
                    left_end = current_source
                    left_range = left_end - left_start
                    currents.extend([left_start, left_range])
                if currents and currents[0] + currents[1] > to_map_end:
                    right_start = current_source + range_map
                    right_end = currents[0] + currents[1]
                    right_range = right_end - right_start
                    currents.extend([right_start, right_range])
            else:
                unmapped.extend(currents[:2])

            currents.pop(0)
            currents.pop(0)

currents = nexts
currents.extend(unmapped)
nexts = []
unmapped = []

actuals = [currents[i] for i in range(0, len(currents), 2)]
print(min(actuals))

# second part 148041808
