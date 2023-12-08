import collections
from enum import IntEnum


def get_score(card):
    # {A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2}
    switch = {
        'A': 13,
        'K': 12,
        'Q': 11,
        'J': 10,
        'T': 9,
        '9': 8,
        '8': 7,
        '7': 6,
        '6': 5,
        '5': 4,
        '4': 3,
        '3': 2,
        '2': 1
    }
    return switch.get(card, "Invalid day01.txt")


class HandType(IntEnum):
    FiveKind = 1
    FourKind = 2
    FullHouse = 3
    ThreeKind = 4
    TwoPair = 5
    OnePair = 6
    HighCard = 7


class Card:
    def __init__(self, s, bid):
        self.bid = int(bid)
        self.hand = s.replace('T', 'B').replace('J', 'C').replace('Q', 'D').replace('K', 'E').replace('A', 'F')
        self.type = self.get_hand_type(self.hand)
        self.rank = 0

    def get_hand_type(self, hand):
        counts = collections.Counter(list(hand))
        values = list(counts.values())

        if 5 in values:
            return HandType.FiveKind
        elif 4 in values:
            return HandType.FourKind
        elif 3 in values and 2 in values:
            return HandType.FullHouse
        elif 3 in values:
            return HandType.ThreeKind
        elif values.count(2) == 2:
            return HandType.TwoPair
        elif 2 in values:
            return HandType.OnePair
        else:
            return HandType.HighCard

    def __eq__(self, other):
        return self.hand == other.hand

    def __lt__(self, other):
        if self.type == other.type:
            return self.hand < other.hand
        return self.type > other.type

    def __repr__(self) -> str:
        return f'{self.hand} {self.bid} {self.type}'


class CardWithJoker(Card):

    def __init__(self, s, bid):
        super().__init__(s, bid)
        self.hand = self.hand.replace('C', '*')
        self.type = self.get_hand_type(self.hand)

    def get_hand_type(self, h):
        if h == '*****':
            return HandType.FiveKind

        counts = collections.Counter(h.replace('*', ''))
        mostCommon = counts.most_common()[0][0]
        newHand = h.replace('*', mostCommon)
        return super().get_hand_type(newHand)


def tests():
    lines = [i for i in open('test-in.txt', 'r').read().split('\n') if i.strip()]

    cards = [card.split(' ') for card in lines]
    # print(cards)
    cards = [Card(a, b) for a, b in cards]
    sortedCards = sorted(cards)
    win = [(rank + 1) * card.bid for rank, card in enumerate(sortedCards)]
    result = sum(win)
    assert result == 6440


def convert(hand):
    hand = list(hand)
    for i in range(len(hand)):
        if hand[i] == 'T':
            hand[i] = 10
        elif hand[i] == 'J':
            hand[i] = 0
        elif hand[i] == 'Q':
            hand[i] = 12
        elif hand[i] == 'K':
            hand[i] = 13
        elif hand[i] == 'A':
            hand[i] = 14
        else:
            hand[i] = int(hand[i])
    # hand.sort(reverse=True)
    return hand


def hand(current_hand, part1=True):
    if part1:
        current_hand = current_hand.replace('J', 'X')

    result_rank = ['J23456789TXQKA'.index(i) for i in current_hand]
    res = []
    for r in 'J23456789TXQKA':
        c = collections.Counter(current_hand.replace('J', r))
        p = tuple(sorted(c.values()))
        # all possible combinations
        t = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)].index(p)
        res.append(t)
    part1 = (max(res), *result_rank)
    # print(part1)
    return (max(res), *result_rank)


if __name__ == '__main__':
    tests()

    # f = open('../inputs/day07.txt', 'r')
    lines = [i for i in open('../inputs/day07.txt', 'r').read().split('\n') if i.strip()]
    # print(lines)
    cards = [card.split(' ') for card in lines]
    # print(cards)
    cards = [Card(a, b) for a, b in cards]
    sortedCards = sorted(cards)

    winner = [(rank + 1) * card.bid for rank, card in enumerate(sortedCards)]
    print(f'part 1: {sum(winner)}')

    cards2 = [card.split(' ') for card in lines]
    cards2 = [CardWithJoker(a, b) for a, b in cards2]

    sortedCards2 = sorted(cards2)
    winner = [(rank + 1) * card.bid for rank, card in enumerate(sortedCards2)]

    print(f'part 2: {sum(winner)}')
