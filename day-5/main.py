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

seed = list(
    map(
        int,
        "3640772818 104094365 1236480411 161072229 376099792 370219099 1590268366 273715765 3224333694 68979978 2070154278 189826014 3855332650 230434913 3033760782 82305885 837883389 177854788 2442602612 571881366".split(),
    )
)

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


# tokens = list(map(int, converter.split()[2:]))
# rangestarts = sorted(tokens[i] for i in range(1, len(tokens), 3))
# newseeds = []
# for start, size in seeds:
#     while size > 0:
#         rangeIndex = find_range(start, tokens)
#         if rangeIndex is None:
#             endrange = findnext(rangestarts, start)
#         else:
#             endrange = tokens[rangeIndex + 1] + tokens[rangeIndex + 2]
#         step = min(endrange - start, size)
#         newseeds.append((transform(start, rangeIndex, tokens), step))
#         size -= step
#         start += step

# min_loc = 2 ** 63 - 1
# seed_index = 0
# while seed_index < len(seeds):
#     # print(seeds[seed_index])
#     # print(seeds[seed_index + 1])
#     i = seeds[seed_index]
#     while i < seeds[seed_index] + seeds[seed_index + 1]:
#         curr = i
#         i = -1
#         for m in map_set:
#             for ranges in m:
#                 if ranges[1] <= curr and (curr - ranges[1]) < ranges[2]:
#                     if i == -1:
#                         i = ranges[1] + ranges[2]
#                     curr = curr - ranges[1] + ranges[0]
#                     break
#         # print(curr)
#         if curr < min_loc:
#             min_loc = curr
#     seed_index += 2
# print(min_loc)
content = [line.strip() for line in data.splitlines()] #[line.strip() for line in open("input05sts")]

currents = []
nexts = [int(i) for i in re.findall('[0-9]+',content[0])]
unmapped = []

input = content[2:]
input = [i for i in input if i != '']

for line in input:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) == 0:
        currents = nexts
        currents.extend(unmapped)
        nexts = []
        unmapped = []
    else:
        currents.extend(unmapped)
        unmapped = []
        numbers = [int(num) for num in numbers]
        current_destination = numbers[0]
        current_source = numbers[1]
        range_map = numbers[2]

        while len(currents) > 0:
            # if currents lower bound falls beneath the current source end and its upper bound falls above the
            # current source start, that means that some or part of its range fits and must be mapped
            if currents[0] < current_source + range_map and currents[0] + currents[1] > current_source:
                # start of part to be mapped
                to_map_start = max(currents[0], current_source)
                # range of part to be mapped
                to_map_end = min(current_source + range_map, currents[0] + currents[1])
                to_map_range = to_map_end - to_map_start

                # to get mapped values, you take to_map_start - current_destination, which gives you the distance
                # from the source start then you take the mapped range and add that to the source start to get
                # the mapped end then you subtract the end from the start to get the range
                mapped_start = current_destination + (to_map_start - current_source)
                mapped_range = to_map_range
                nexts.append(mapped_start)
                nexts.append(mapped_range)

                # if the to be mapped start is the current destination and the current start and current
                # destination are not the same there's some part of the current range that needs to be cut
                if currents[0] < to_map_start:
                    left_start = currents[0]
                    left_end = current_source
                    left_range = left_end - left_start
                    currents.append(left_start)
                    currents.append(left_range)

                # same thing, but on the right
                if currents[0] + currents[1] > to_map_end:
                    right_start = current_source + range_map
                    right_end = currents[0] + currents[1]
                    right_range = right_end - right_start
                    currents.append(right_start)
                    currents.append(right_range)
            else:
                unmapped.append(currents[0])
                unmapped.append(currents[1])

            currents.pop(0)
            currents.pop(0)

currents = nexts
currents.extend(unmapped)
nexts = []
unmapped = []

actuals = [currents[i] for i in range(0, len(currents), 2)]
print(min(actuals))

# second part 148041808
