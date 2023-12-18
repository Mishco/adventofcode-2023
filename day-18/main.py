
if __name__ == '__main__':
    data = open('sample').read().strip().splitlines()

    for item in data:
        direction, deep, colour = item.split()
        # print(direction, deep)

        match direction:
            case 'U':
                print('up')
            case 'D':
                print('down')
            case 'L':
                print('left')
            case 'R':
                print('right')

        print(deep)

