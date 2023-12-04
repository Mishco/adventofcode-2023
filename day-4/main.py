# --- Day 4: Scratchcards ---

test_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

total_part_1 = 0

content = open('../inputs/day04.txt').read()
for line in content.splitlines():
    cards = line.split('|')
    winning = cards[0].split()[2:]
    others = cards[1].split()
    matches = set(winning) & set(others)
    num_matches = 2 ** (len(matches) - 1) if len(matches) > 0 else 0
    total_part_1 += int(num_matches)

print(total_part_1)  # 24706
# 41845 not

lines = content.splitlines()
cards = [1] * len(lines)
for idx, ln in enumerate(lines):
    x, y = map(str.split, ln.split('|'))
    count_of_same = len(set(x) & set(y))
    for j in range(idx + 1, min(idx + 1 + count_of_same, len(lines))):
        cards[j] += cards[idx]

print(sum(cards))  # 13114317
