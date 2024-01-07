sample = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


card_score = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

card_score_w_joker = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': -1,
    'Q': 10,
    'K': 11,
    'A': 12
}


hand_score = {
    "5ok": 6,
    "4ok": 5,
    "fh": 4,
    "3ok": 3,
    "2p": 2,
    "1p": 1,
    "hc": 0,
}


def get_hand_type(hand, with_joker=False):
    card_counts = {"A": 0}
    joker_count = 0
    for card in hand:
        if with_joker and card == "J":
            joker_count += 1
            continue
        if card not in card_counts:
            card_counts[card] = 0
        card_counts[card] += 1
    card_counts = sorted(card_counts.values())
    card_counts[-1] += joker_count
    if card_counts[-1] == 5:
        return "5ok"
    elif card_counts[-1] == 4:
        return "4ok"
    elif card_counts[-2:] == [2, 3]:
        return "fh"
    elif card_counts[-1] == 3:
        return "3ok"
    elif card_counts[-2:] == [2, 2]:
        return "2p"
    elif card_counts[-1] == 2:
        return "1p"
    else:
        return "hc"


def get_hand_order(hand, with_joker=False):
    hand_type = get_hand_type(hand, with_joker=with_joker)
    if with_joker:
        card_scores = [card_score_w_joker[card] for card in hand]
    else:
        card_scores = [card_score[card] for card in hand]
    return tuple([hand_score[hand_type]] + card_scores)


def get_parsed_hands(lines, with_joker=False):
    parsed_hands = []
    for line in lines:
        hand, bid = line.split(' ')
        parsed_hands.append((get_hand_order(hand, with_joker=with_joker), bid))
    return parsed_hands


def get_winnings(lines, with_joker=False):
    parsed_hands = get_parsed_hands(lines, with_joker)
    winnings = 0
    for i, hand in enumerate(sorted(parsed_hands)):
        winnings += (i + 1) * int(hand[1])
    return winnings


def main():
    print("sample 1:", get_winnings(sample))
    print("sample 2:", get_winnings(sample, with_joker=True))

    with open("inputs/day_7.txt") as f:
        lines = f.readlines()
    print("part 1:", get_winnings(lines))
    print("part 2:", get_winnings(lines, with_joker=True))

if __name__ == "__main__":
    main()