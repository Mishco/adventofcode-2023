"""
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
114 (top right) and 58 (middle right).
 Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
"""

test_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

games = {}

# for each_line in test_input.splitlines():
#     print(each_line)


# schematic = test_input
schematic = []
part_number = []
total = 0
symbols = ["*", "#", "+", "$", "%"]

with (open('../inputs/day03.txt', mode='r') as f):
    for rows in f:
        schematic.append(rows)
lists = []
special_list = []
gears_list = []

# Split the schematic into rows
rows = schematic #.split()
gears = 0
# Initialize the sum of part numbers to 0
part_sum = 0

for i in range(len(rows)):
    # Loop through each character in the row
    j = 0
    while j < len(rows[i]):
        # Check if the character is a number
        if rows[i][j].isdigit():
            # Check if the number is adjacent to a symbol in any of the eight directions
            gear_adjacent = False
            adjacent = False
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if i + x < 0 or i + x >= len(rows) or j + y < 0 or j + y >= len(rows[i]):
                        continue
                    if rows[i + x][j + y] in ['#', '+', '$', '@', '%', '/', '-', '=', '!', '^', '&']:
                        adjacent = True
                        break
                    if rows[i + x][j + y] in ['*']:
                        gear_adjacent = True
                        break
                if adjacent or gear_adjacent:
                    break
            # Add the number to the sum of part numbers if it is adjacent to a symbol
            if adjacent or gear_adjacent:
                # Find the end of the part number in the forward direction
                end = j + 1
                while end < len(rows[i]) and rows[i][end].isdigit():
                    end += 1
                # Find the end of the part number in the backward direction
                start = j - 1
                while start >= 0 and rows[i][start].isdigit():
                    start -= 1
                # Add the part number to the sum
                lists.append(int(rows[i][start + 1:end]))
                part_sum += int(rows[i][start + 1:end])

                if gear_adjacent:
                    special_list.append(rows[i][start + 1:end])
                    # print(i, start + 1, end)
                    gears_list.append({
                        'i': i,
                        'start': start + 1,
                        'end': end,
                        'value': rows[i][start + 1:end]
                    })
                    if len(special_list) >= 2:
                        if special_list[0].endswith('*') or special_list[1].endswith('*'):
                            part_sum += sum(special_list)
                            special_list = []
                            gear_adjacent = False  # founded and remove
                        else:
                            first_gear = int(special_list[0].replace('.', ''))
                            second_gear = int(special_list[1])

                            first_info = next(item for item in gears_list if item["value"] == str(first_gear))
                            second_info = next(item for item in gears_list if item["value"] == str(second_gear))

                            if abs(first_info['i']-second_info['i']) >2:
                                # remove first and sum
                                special_list = []
                                part_sum += first_gear
                                first_gear = 1
                                continue

                            gears += first_gear * second_gear
                            special_list = []
                            gear_adjacent = False  # founded and remove
                # gears.append(rows[i][start + 1:en

                # Move the index to the end of the part number
                j = end
            else:
                j += 1

            # Add the number to the sum of part numbers if it is adjacent to a symbol
            # elif gear_adjacent:
            #     end = j + 1
            #     while end < len(rows[i]) and rows[i][end].isdigit():
            #         end += 1
            #     start = j - 1
            #     while start >= 0 and rows[i][start].isdigit():
            #         start -= 1
            # Add the part number to the sum
            # special_list.append(rows[i][start + 1:end])
            # gears_list.append(rows[i][start + 1:end])
            # if len(special_list) >=2:
            #     if special_list[0].endswith('*') or special_list[1].endswith('*'):
            #         part_sum += sum(special_list)
            #         special_list = []
            #     else:
            #         gears += int(special_list[0].replace('.','')) * int(special_list[1])
            #         special_list = []
            # # gears.append(rows[i][start + 1:end])
            # part_sum += int(rows[i][start + 1:end])
            # Move the index to the end of the part number
            #     j = end
            # else:
            #     j += 1
        else:
            j += 1

# Print the sum of part numbers
print(f"{lists=}")
print(f"{gears_list=}")
# print(gears)
# print(part_sum)

print(f"{gears=}")
print(f"{part_sum=}")

print(gears + part_sum)

# 436155 too low
# 515997 too low

# 535351 -correct

# 87287096 should be correct
