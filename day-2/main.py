import re

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

with (open('../day-1/input', mode='r') as f):
    for line in f:
        # line = '1sevenninesix1\n'
        # line = '5bszzkpcdxqkvkf7tgcone2'
        # line = '5bszzkpcdxqkvkf7tgcone2'
        # line = '6oneightsr' ## 68 and not 61
        # line = 'four2prxrhrcvfour' ## 44 and not 42
        # line = '4threelfvzndfive'
        # line = '7zmlcpsjneight7pbtqbkgl' # should be 77 not 78
        # line ='5bszzkpcdxqkvkf7tgcone2'
        # line= '1twoonefivenvvhjf'
        # line = 'bjckqhbnthreethreeonervtkdvxkgf43' # should 33, not 31
        # line = 'onexlqp3bhh'
        # line = 'glvctfourgmlrqbpsevenvksevensix9' # should 49, not 46
        # line = 'geightwodd88ctqzfourfivesix1six' # 86
        # print(line)

        m = re.search(r"\d", line)
        m2 = re.search(r"\d", line[::-1])

        firs_real_digit = re.findall('\d', line)[:1]
        last_real_digit = re.findall('\d', line[::-1])[:1]

        matches = re.finditer(r'\d', line)
        indices = [match.start() for match in matches]

        first_digit_indx = line.index(firs_real_digit[0]) if firs_real_digit else 0
        m2_digit_indx = indices[-1:][0] if len(indices) >= 1 else 0

        old_pattern = "\W*(one|two|three|four|five|six|seven|eight|nine)\W*"
        new_pattern = "(?=(one|two|three|four|five|six|seven|eight|nine))"

        re_digits_words_first = re.findall(new_pattern, line)[:1]
        re_digits_words_last = re.findall(new_pattern, line)[-1:]

        iter = re.finditer(new_pattern, line)
        indices_for_words = [m.start(0) for m in iter]

        if re_digits_words_first:
            re_digits_words_first_index = line.index(re_digits_words_first[0])
        if re_digits_words_last:
            re_digits_words_last_index = indices_for_words[-1:][0]

        if m and m2 and not re_digits_words_first and not re_digits_words_last:
            first_digit = line[m.start()]
            last_digit = line[::-1][m2.start()]
            act_val = str(first_digit) + str(last_digit)

        elif m and (first_digit_indx <= re_digits_words_first_index) and (m2_digit_indx >= re_digits_words_last_index):
            first_digit = line[m.start()]
            last_digit = line[::-1][m2.start()]
            act_val = str(first_digit) + str(last_digit)

        elif m2 and (first_digit_indx <= re_digits_words_first_index) and (m2_digit_indx >= re_digits_words_last_index):
            first_digit = line[m.start()]
            last_digit = line[::-1][m2.start()]
            act_val = str(first_digit) + str(last_digit)

        elif m and re_digits_words_last and (first_digit_indx <= re_digits_words_first_index) and (
                m2_digit_indx <= re_digits_words_last_index):
            first_digit = line[m.start()]
            words_digit_second = get_number_from_word(re_digits_words_last[0])
            act_val = str(first_digit) + str(words_digit_second)

        elif re_digits_words_first and m2 and (m2_digit_indx >= re_digits_words_last_index) and (
                first_digit_indx <= re_digits_words_first_index):
            words_digit_first = get_number_from_word(re_digits_words_first[0].strip())
            last_digit = line[::-1][m2.start()]
            act_val = str(words_digit_first) + str(last_digit)

        elif m2_digit_indx == first_digit_indx and re_digits_words_first and m2 and (
                m2_digit_indx >= re_digits_words_last_index):
            words_digit_first = get_number_from_word(re_digits_words_first[0].strip())
            last_digit = line[::-1][m2.start()]
            act_val = str(words_digit_first) + str(last_digit)

        elif re_digits_words_first and m2 and (m2_digit_indx >= re_digits_words_last_index) and (
                first_digit_indx > re_digits_words_first_index):
            words_digit_first = get_number_from_word(re_digits_words_first[0].strip())
            last_digit = line[::-1][m2.start()]
            act_val = str(words_digit_first) + str(last_digit)

        elif re_digits_words_first and re_digits_words_last:
            words_digit_first = get_number_from_word(re_digits_words_first[0].strip())
            words_digit_second = get_number_from_word(re_digits_words_last[0].strip())
            act_val = str(words_digit_first) + str(words_digit_second)

        print(f"{line=}")
        print(act_val)
        sum += int(act_val)
        first_digit = 0
        last_digit = 0
        words_digit_first = 0
        words_digit_second = 0
        act_val = 0

print(sum)

# 54455 not right
# 54417 not right
# 54535 not right
# 54340 not right
# 54673
# 54397
# 54390
# 54492
# 54414
# 54427
# 54431

# total=54431 is right
