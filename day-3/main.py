import itertools
import re

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

part_number = []
total = 0
symbols = ["*", "#", "+", "$", "%"]
schematic = []

with (open('input', mode='r') as f):
    for rows in f:
        schematic.append(rows)
# Split the schematic into rows
# rows = schematic.split()
lists = []
# Split the schematic into rows
rows = schematic #.split()

# Initialize the sum of part numbers to 0
part_sum = 0


for i in range(len(rows)):
    # Loop through each character in the row
    j = 0
    while j < len(rows[i]):
        # Check if the character is a number
        if rows[i][j].isdigit():
            # Check if the number is adjacent to a symbol in any of the eight directions
            adjacent = False
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if i+x < 0 or i+x >= len(rows) or j+y < 0 or j+y >= len(rows[i]):
                        continue
                    if rows[i+x][j+y] in ['*', '#', '+', '$', '@', '%', '/', '-', '=','!','^','&']:
                        adjacent = True
                        break
                if adjacent:
                    break
            # Add the number to the sum of part numbers if it is adjacent to a symbol
            if adjacent:
                # Find the end of the part number in the forward direction
                end = j + 1
                while end < len(rows[i]) and rows[i][end].isdigit():
                    end += 1
                # Find the end of the part number in the backward direction
                start = j - 1
                while start >= 0 and rows[i][start].isdigit():
                    start -= 1
                # Add the part number to the sum
                lists.append(int(rows[i][start+1:end]))
                part_sum += int(rows[i][start+1:end])
                # Move the index to the end of the part number
                j = end
            else:
                j += 1
        else:
            j += 1

# Print the sum of part numbers
print(lists)
print(part_sum)


# 436155 too low
# 515997 too low

# 535351 -correct

