import re

# Your calculation isn't quite right.
# It looks like some of the digits are actually spelled out with letters:
# one, two, three, four, five, six, seven, eight, and nine
# also count as valid "digits".

sum = int(0)


def get_number_from_word(word):
    switch = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return switch.get(word, "Invalid input")


test_input = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

with open('../day-1/input', mode='r') as f:
    for line in f:
        # line = '1sevenninesix1\n'
        # line = '5bszzkpcdxqkvkf7tgcone2'
        line ='4nineeightseven2'
        print(line)

        m = re.search(r"\d", line)
        m2 = re.search(r"\d", line[::-1])

        mmm = re.findall(r"\d",line )
        re_digits_words = re.search("\W*(one|two|three|four|five|six|seven|eight|nine)\W*", line)
        re_digits_words_first = re.findall("\W*(one|two|three|four|five|six|seven|eight|nine)\W*", line)[:1]
        re_digits_words_last = re.findall("\W*(one|two|three|four|five|six|seven|eight|nine)\W*", line)[-1:]

        re_digits_words_first_index = [(m.start(0), m.end(0)) for m in re.finditer(re_digits_words_first[0], line)]
        re_digits_words_last_index = [(m.start(0), m.end(0)) for m in re.finditer(re_digits_words_last[0], line)]


        if m and m2 and not re_digits_words_first and not re_digits_words_last:
            first_digit = line[m.start()]
            last_digit = line[::-1][m2.start()]
            act_val = str(first_digit) + str(last_digit)

        elif m.lastindex < re_digits_words_first_index[0][0]:
            first_digit = line[m.start()]
            last_digit = line[::-1][m2.start()]
            act_val = str(first_digit) + str(last_digit)

        elif re_digits_words_first and re_digits_words_last:
            words_digit_first = get_number_from_word(re_digits_words_first[0].strip())
            words_digit_second = get_number_from_word(re_digits_words_last[0].strip())
            act_val = str(words_digit_first) + str(words_digit_second)

        elif m and re_digits_words_last:
            first_digit = line[m.start()]
            words_digit_second = get_number_from_word(re_digits_words_last[0])
            act_val = str(first_digit) + str(words_digit_second)

        elif re_digits_words_first and m2:
            words_digit_first = get_number_from_word(re_digits_words_first[0].strip())
            last_digit = line[::-1][m2.start()]
            act_val = str(words_digit_first) + str(last_digit)


        # print(first_digit, last_digit)
        print(act_val)
        sum += int(act_val)
        first_digit = 0
        last_digit = 0
        words_digit_first = 0
        words_digit_second = 0

print(sum)
