### --- Day 9: Mirage Maintenance ---

if __name__ == '__main__':

    ttt ="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

    # lines  = ttt.splitlines()
    # print(lines)

    lines = [[int(i) for i in s.split()] for s in open('../inputs/day09.txt', 'r').read().split('\n') if s.strip()]
    print(lines)
    # l = [[int(i) for i in s.split()] for s in open('input').read().split('\n') if s.strip()]


    def n(l):
        if sum(i != 0 for i in l) == 0:
            return 0
        m = []
        for i in range(len(l) - 1):
            m.append(l[i + 1] - l[i])
        return l[-1] + n(m)


    print(sum(n(i) for i in lines))
    print(sum(n(i[::-1]) for i in lines))

    ###########################################

    tot = 0
    tot2 = 0
    for line in open('../inputs/day09.txt', 'r').read().split('\n'):
        digits = [int(x) for x in line.split()]
        grid = [digits]
        while len(set(grid[-1])) > 1:
            next_line = [grid[-1][i + 1] - grid[-1][i] for i in range(len(grid[-1]) - 1)]
            grid.append(next_line)
        k = grid[-1][0]
        k2 = k
        for i in range(len(grid) - 2, -1, -1):
            k += grid[i][-1]
            k2 = grid[i][0] - k2
        tot += k
        tot2 += k2

    print(tot)
    print(tot2)