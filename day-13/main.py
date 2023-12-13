# 100 multiplied by the number of rows
MULTIPLIED_FOR_ROWS: int = 100


def transpose(input_matrix):
    # return [*zip(*input_matrix)]
    return list(map(list, zip(*input_matrix)))


def reflect_pattern(p, s):
    for i in range(1, len(p)):
        diff_count = sum(c1 != c2 for r1, r2 in zip(p[i - 1::-1], p[i:]) for c1, c2 in zip(r1, r2))
        if diff_count == s:
            return i
    return 0


if __name__ == '__main__':
    lines = list(map(str.splitlines, open('../inputs/day13.txt').read().split('\n\n')))

    for s in 0, 1:
        # for each line: 100 * rows + cols
        res = sum(
            MULTIPLIED_FOR_ROWS * reflect_pattern(line, s) + reflect_pattern(transpose(line), s) for line in lines)
        print(f"part {s}: {res}")
