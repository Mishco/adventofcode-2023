import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque

def main():
    pass

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Define a function to print the board
def print_board(board):
    for row in board:
        print(row)

def is_valid_position(board, row, col):
    return row >= 0 and row < len(board) and col >= 0 and col < len(board)

# def move_rock(board, row, col, direction):
#     # Check if the rock can be moved in the given direction
#     # Loop through all the rocks on the board
#     for row in range(len(board)):
#         for col in range(len(board[row])):
#             if board[row][col] == "O":
#                 row_offset, col_offset = directions[direction]
#                 new_row = row + row_offset
#                 new_col = col + col_offset
#                 if is_valid_position(board, new_row, new_col) and board[new_row][new_col] == ".":
#                     # Move the rock to the new position
#                     # board[row] = board[row][:col] + "." + board[row][col+1:]
#                     board[row] = "".join(list(board[row][:col]) + ["."] + list(board[row][col + 1:]))
#                     board[new_row] = "".join(list(board[new_row][:new_col] + "O" + board[new_row][new_col+1:]))
#                 # Print an error message if the rock cannot be moved
#                 else:
#                     print("Cannot move rock at position ({}, {})".format(row, col))


def tilt_platform(board, directionslist= ['up', 'left', 'down', 'right'], max_cycles=1000000000):
    # Define the row and column offsets for each direction
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    # Loop through all the rocks on the board
    cycles = 0
    while cycles < max_cycles:
        cycles += 1
        moved = False
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "O":
                    for direction in directionslist:
                        row_offset, col_offset = directions[direction]
                        new_row = row + row_offset
                        new_col = col + col_offset
                        if is_valid_position(board, new_row, new_col) and board[new_row][new_col] == ".":
                            board[row][col] = "."
                            board[new_row][new_col] = "O"
                            row, col = new_row, new_col
                            moved = True
                            break
                    if moved:
                        break
            if moved:
                break
        if not moved:
            break

    # Calculate the total load on the north support beams
    north_load = 0
    total_rows = len(board)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "O":
                north_load += total_rows - row
    print(north_load)
    return north_load

# 50
# 18
# 32
# 21
# 12
# 3
# =136
if __name__ == '__main__':
    # main()
    # The total load is the sum of the load caused by all of the rounded rocks.
    # In this example, the total load is 136.
    #
    # Tilt the platform so that the rounded rocks all roll north.
    # Afterward, what is the total load on the north support beams?

    data = open('sample').read().strip()
    # data = open('../inputs/day14.txt').read().strip()
    L = data.split('\n')
    board = [[c for c in row] for row in L]
    # print_board(board)
    print(tilt_platform(board, directionslist=["up"])) # part1
    print(tilt_platform(board, directionslist=['up', 'left', 'down', 'right'])) # part1

    # print_board(board)
    # part1
    # 98143 not right
    # 106186 is right

# 106390 for part2

