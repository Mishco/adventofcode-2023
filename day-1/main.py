import re

# test_input = """
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# """
# for line in test_input.splitlines():
# print(line)

sum = int(0)

with open('input', mode='r') as f:
    for line in f:
        m = re.search(r"\d", line)
        m2 = re.search(r"\d", line[::-1])

        first_digit = line[m.start()]
        last_digit = line[::-1][m2.start()]
        # print(first_digit, last_digit)
        act_val = str(first_digit) + str(last_digit)
        sum += int(act_val)

print(sum)
