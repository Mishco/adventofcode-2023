import collections

test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

games = {}

with (open('../inputs/day02.txt', mode='r') as f):
    for each_line in f:
    # for each_line in test_input.splitlines():
        if 'Game' in each_line:
            game_id = each_line.split(":")[0]
            ls_ = each_line.split(":")[1]
            if game_id is not []:
                games[game_id] = ls_

print(games)

red_values = []
blue_values = []
green_values = []

new_games = collections.defaultdict(list)
games.items()

for game_id, game in games.items():
    for item in game.split(';'):
        for value in item.split(','):
            if 'red' in value:
                # print(value)
                red_values.append(int(value.strip().split(' ')[0]))
            elif 'blue' in value:
                # print()
                blue_values.append(int(value.strip().split(' ')[0]))

            elif 'green' in value:
                green_values.append(int(value.strip().split(' ')[0]))

    new_games[game_id].append({'blue': blue_values})
    new_games[game_id].append({'green': green_values})
    new_games[game_id].append({'red': red_values})
    red_values = []
    blue_values = []
    green_values = []

print("Red values:", red_values)
print("Blue values:", blue_values)
print("Green values:", green_values)

# The Elf would first like to know which games
# would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

minimal_green = 13
minimal_red = 12
minimal_blue = 14

# possible_games = collections.defaultdict(list)
sum = 0
total_power = 0
for key, val in new_games.items():
    print(key, val)
    # print(val)
    max_blue, max_red, max_green = 0, 0, 0
    for invalue in val:
        if 'blue' in invalue.keys():
            max_blue = max(invalue['blue'])
            min_blue = min(invalue['blue'])
        elif 'green' in invalue.keys():
            max_green = max(invalue['green'])
            min_green = min(invalue['green'])
        elif 'red' in invalue.keys():
            max_red = max(invalue['red'])
            min_red = min(invalue['red'])

    print(max_red, max_green, max_blue)
    # print(min_red, min_green, min_blue)
    power = max_red * max_green * max_blue
    print(power)
    total_power += power
    if minimal_red >= max_red and minimal_green >= max_green and minimal_blue >= max_blue:
        print(f"{key} would be possible")
        just_number = key.split(' ')[1]
        sum += int(just_number)

print()
# print(sum)
print(total_power)
# 2350 - not rigtr
# 2439
