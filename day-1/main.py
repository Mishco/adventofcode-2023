import re

# test_input = """
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# """
#for line in test_input.splitlines():
    # print(line)

sum = 0

with open('input', mode='r') as f:
    # all_lines = f.readlines()

    for line in f:
    # for line in f.readlines():
        print(line)
        m = re.search(r"\d", line)
        m2 = re.search(r"\d", line[::-1])
        
        first_digit = line[m.start()]
        last_digit = line[::-1][m2.start()]
        print(first_digit, last_digit)
        sum += int(first_digit) + int(last_digit)

print(sum)