import re

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

sum = 0


def get_num_matches_for_game(winning_numbers: list, my_numbers: list) -> int:
    reached_win_end = False
    reached_my_end = False
    matched = 0

    i = 0
    j = 0
    # with find this would've been much shorter, but I wanted
    # to implement a more optimized solution where you start
    # at the beginnings of both arrays and then based on the
    # comparison of the numbers, you either increase the iterator
    # of one of the arrays, or both of them until you reach the ends
    while not reached_win_end or not reached_my_end:
        win_num = winning_numbers[i]
        my_num = my_numbers[j]
        increase_i = False
        increase_j = False

        if win_num == my_num:
            matched += 1
            increase_i = True
            increase_j = True

        elif win_num < my_num:
            if not reached_win_end:
                increase_i = True
            else:
                increase_j = True

        else:
            if not reached_my_end:
                increase_j = True
            else:
                increase_i = True

        if increase_i:
            if i < len(winning_numbers) - 1:
                i += 1
            else:
                reached_win_end = True

        if increase_j:
            if j < len(my_numbers) - 1:
                j += 1
            else:
                reached_my_end = True

    return matched


num_cards = [1 for _ in range(len(lines))]

for i in range(len(lines)):
    all_numbers = lines[i].split(": ")[1].split(" | ")

    winning_numbers = sorted(int(num) for num in all_numbers[0].split())
    my_numbers = sorted(int(num) for num in all_numbers[1].split())

    matched = get_num_matches_for_game(winning_numbers, my_numbers)

    if matched != 0:
        for j in range(i + 1, i + 1 + matched):
            num_cards[j] += num_cards[i]

    sum += num_cards[i]

print(sum)
