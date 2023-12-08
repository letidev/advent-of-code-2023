import functools

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

card_powers = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14
}


def calc_hand_type(hand: str):
    sorted_hand = sorted(hand)

    types_of_same = []
    count = 1
    jokers = 0
    hand_sz = len(sorted_hand)

    for i in range(hand_sz):
        if (sorted_hand[i] == "J"):
            jokers += 1

        if i + 1 < hand_sz and sorted_hand[i] == sorted_hand[i+1] and sorted_hand[i] != "J":
            count += 1
        else:
            if count > 1:
                types_of_same.append(count)
            count = 1

    types_of_same = sorted(types_of_same)
    types_of_same.reverse()

    if types_of_same == []:
        if jokers < 5:
            types_of_same = [1 + jokers]
        else:
            types_of_same = [5]
    else:
        types_of_same[0] += jokers

    if types_of_same == [5]:  # type 7
        return 7  # 22222
    #
    elif types_of_same == [4]:  # type 6
        return 6  # 22223
    #
    elif types_of_same == [3, 2]:  # type 5
        return 5  # 22333
    #
    elif types_of_same == [3]:  # type 4
        return 4  # 22234
    #
    elif types_of_same == [2, 2]:  # type 3
        return 3  # 22334
    #
    elif types_of_same == [2]:  # type 2
        return 2  # 22345
    #
    else:  # type 1
        return 1  # 23456


class Hand:
    def __init__(self, hand, bid, hand_type) -> None:
        self.hand = hand
        self.bid = bid
        self.hand_type = hand_type

    def __str__(self) -> str:
        return f"hand: {self.hand} bid: {self.bid} hand_type: {self.hand_type}"


def cmp_fn(x: Hand, y: Hand):
    if x.hand_type != y.hand_type:
        return x.hand_type - y.hand_type

    for i in range(len(x.hand)):
        if x.hand[i] != y.hand[i]:
            return card_powers[x.hand[i]] - card_powers[y.hand[i]]

    return 0


hands = []

for line in lines:
    split = line.split()

    hand = split[0]
    bid = split[1]
    hand_type = calc_hand_type(hand)
    hands.append(Hand(hand, bid, hand_type))

sorted_hands = sorted(hands, key=functools.cmp_to_key(cmp_fn))

sum = 0
for i in range(len(sorted_hands)):
    print(sorted_hands[i])
    sum += (i+1) * int(sorted_hands[i].bid)

print(sum)
