# --- Day 13: Point of Incidence ---
import numpy as np

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


def run_with_numpy(lines):
    print('\nrun with numpy:\n')
    grids = [
        np.array([[int(x) for x in line] for line in ln.replace(".", "0").replace("#", "1").split("\n")])
        for ln in lines
    ]

    for diffs in (0, 1):
        result = 0
        for g in grids:
            for g, f in ((g, 1), (g.T, MULTIPLIED_FOR_ROWS)):
                for c in range(0, g.shape[1] - 1):
                    ln = min(c + 1, g.shape[1] - c - 1)
                    part_first = np.flip(g[:, c - ln + 1: c + 1], axis=1)
                    part_second = g[:, c + 1: c + 1 + ln]
                    count_not_equal_items = np.sum(part_first != part_second)
                    if count_not_equal_items == diffs:
                        result += (c + 1) * f
                        break
        print(f"part {diffs}: {result}")


if __name__ == '__main__':
    orig_lines: list[str] = open('../inputs/day13.txt').read().split('\n\n')
    lines = list(map(str.splitlines, orig_lines))

    for s in 0, 1:
        res = sum(
            MULTIPLIED_FOR_ROWS * reflect_pattern(line, s) + reflect_pattern(transpose(line), s) for line in lines)
        print(f"part {s}: {res}")

    run_with_numpy(orig_lines)
