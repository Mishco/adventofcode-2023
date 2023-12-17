def energized(entry: int, direction: complex) -> int:
    """
    breadth-first search algorithm to traverse a board and count the number of cells
    that can be reached from the starting cell entry by following a path of arrows.
    The arrows are represented by the characters |, -, /, and \ in the board dictionary.
    """
    queue = [(entry - direction, direction)]
    visited = set()
    while queue:
        current_z, direction = queue.pop()
        if (current_z, direction) in visited:
            continue
        visited.add((current_z, direction))
        newz = current_z + direction
        if newz not in board:
            continue
        match board[newz]:
            case "|" if direction.imag:
                new_dir = [1, -1]
            case "-" if direction.real:
                new_dir = [1j, -1j]
            case "/":
                new_dir = [(direction * 1j).conjugate()]
            case "\\":
                new_dir = [(direction * -1j).conjugate()]
            case _:
                new_dir = [direction]
        queue += [(newz, new_direction) for new_direction in new_dir]
    return len({x[0] for x in visited}) - 1


if __name__ == '__main__':
    # ls = open('sample').read().strip().split('\n')
    ls = open("../inputs/day16.txt").read().strip().split('\n')

    board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}

    print(energized(0, 1j))  # Part 1, 7477

    N, M = len(ls), len(ls[0])
    entries = [(i, 1j) for i in range(N)]
    entries += [(i + (M - 1) * 1j, -1j) for i in range(N)]
    entries += [(i * 1j, 1) for i in range(M)]
    entries += [(N - 1 + i * 1j, -1) for i in range(M)]
    print(max(energized(*x) for x in entries))  # Part 2
