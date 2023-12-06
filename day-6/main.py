# and # 27102791


def calculate(times, dist):
    ret = 1
    for time, distance in zip(times, dist):
        wins = 0
        for i in range(time):
            if i * (time - i) > distance:
                wins += 1
        ret *= wins
    return ret


def run_tests():
    test = """Time:      7  15   30
    Distance:  9  40  200
    """
    val = [x.strip("\r\n") for x in test.splitlines()]
    ttt = map(int, val[0].split(':')[1].split())
    ddd = map(int, val[1].split(':')[1].split())
    assert calculate(ttt, ddd) == 288, "should be 288"


if __name__ == '__main__':
    run_tests()

    f = open('../inputs/day06.txt', 'r')
    values = [x.strip("\r\n") for x in f.readlines()]
    times = map(int, values[0].split(':')[1].split())
    distances = map(int, values[1].split(':')[1].split())

    print(calculate(times, distances))  # 3316275 is right answer

    times = map(int, values[0].split(':')[1].replace(' ', '').split())
    distances = map(int, values[1].split(':')[1].replace(' ', '').split())

    print(calculate(times, distances))  # 27102791 is right
