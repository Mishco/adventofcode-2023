# 100 multiplied by the number of rows
MULTIPLIED_FOR_ROWS: int = 100


def read_lines_from_file(file_path):
    """
    Reads lines from a file, trims whitespace, and ignores empty lines.

    Args:
    file_path (str): The path to the file to be read.

    Returns:
    list of str: The lines from the file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def read_lines_from_file(file_path, delimiter=None):
    """
    Reads lines from a file, trims whitespace, and optionally splits each line by a delimiter.

    Args:
    file_path (str): The path to the file to be read.
    delimiter (str, optional): The delimiter to split each line. Default is None.

    Returns:
    list of str or list of list of str: The lines from the file, optionally split by the delimiter.
    """
    with open(file_path, 'r') as file:
        if delimiter:
            return [line.strip().split(delimiter) for line in file if line.strip()]
        else:
            return [line.strip() for line in file if line.strip()]


def reflect_pattern(pattern, does_not_match=0):
    pattern = ["".join(x) for x in pattern]

    for i in range(len(pattern) - 1):
        places_where_doesnt_work = 0
        for j in range(len(pattern)):
            if i + 1 + (i - j) in range(len(pattern)) and pattern[j] != pattern[i + 1 + (i - j)]:
                places_where_doesnt_work += len(
                    [k for k in range(len(pattern[j])) if pattern[j][k] != pattern[i + 1 + (i - j)][k]])
        if places_where_doesnt_work == does_not_match:
            return i
    return None

    # rows = len(pattern)
    # cols = len(pattern[0])
    # reflected_pattern = [''] * rows

    # if rows == cols:
    #     # square pattern, reflect vertically
    #     for i in range(rows):
    #         for j in range(cols):
    #             reflected_pattern[i] += pattern[i][cols - j - 1]
    # elif rows > cols:
    #     # rectangular pattern, reflect horizontally
    #     for i in range(rows):
    #         reflected_pattern[rows - i - 1] = pattern[i]
    # else:
    #     # rectangular pattern, reflect vertically
    #     for i in range(rows):
    #         for j in range(cols):
    #             reflected_pattern[i] += pattern[i][cols - j - 1]
    #
    # return reflected_pattern


def transpose(input_matrix):
    return list(map(list, zip(*input_matrix)))


def reflect_pattern(p, s):
    for i in range(1, len(p)):
        if sum(c1 != c2 for r1, r2 in zip(p[i - 1::-1], p[i:])
               for c1, c2 in zip(r1, r2)) == s: return i
    else:
        return 0


if __name__ == '__main__':
    # lines = open('../inputs/day13.txt', 'r').read().split('\n')
    lines = list(map(str.splitlines, open('../inputs/day13.txt').read().split('\n\n')))

    # lines = open('sample', 'r').read()#.split('\n')
    # lines = open('sample').read().strip().split('\n\n')
    # lines = read_lines_from_file('sample')
    print(lines)

    # count= 0
    # for i, ln in enumerate(lines):
    #     pattern = [list(x) for x in ln.split('\n')]
    #     row = reflect_pattern(pattern, does_not_match=0)
    #     if row is not None:
    #         count += 100 * (row + 1)
    #     col = reflect_pattern(transpose(pattern), does_not_match=0)
    #     if col is not None:
    #         count += (col + 1)
    #
    # print(count)

    # 3182 not right
    # lines = list(map(str.splitlines, open('../inputs/day13.txt').read().split('\n\n')))
    # print(lines)

    for s in 0, 1:
        res = sum(
            MULTIPLIED_FOR_ROWS * reflect_pattern(line, s) + reflect_pattern(transpose(line), s) for line in lines)
        print(f"part {s}: {res}")
