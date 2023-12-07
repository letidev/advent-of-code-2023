import functools

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

card_powers = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def calc_hand_type(hand: str):
    sorted_hand = sorted(hand)

    types_of_same = []
    count = 1
    for i in range(len(sorted_hand) - 1):
        if sorted_hand[i] == sorted_hand[i+1]:
            count += 1
        else:
            if count > 1:
                types_of_same.append(count)
            count = 1

    if count > 1:
        types_of_same.append(count)

    types_of_same = sorted(types_of_same)

    if types_of_same == [5]:
        return 7
    elif types_of_same == [4]:
        return 6
    elif types_of_same == [2, 3]:
        return 5
    elif types_of_same == [3]:
        return 4
    elif types_of_same == [2, 2]:
        return 3
    elif types_of_same == [2]:
        return 2
    else:
        return 1


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

for hand in hands:
    print(hand)

print()
print("======")
print()

sorted_hands = sorted(hands, key=functools.cmp_to_key(cmp_fn))

sum = 0
for i in range(len(sorted_hands)):
    print(sorted_hands[i])
    sum += (i+1) * int(sorted_hands[i].bid)

print(sum)
