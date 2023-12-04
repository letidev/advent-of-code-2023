import re

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

sum = 0

for line in lines:
    all_numbers = line.split(": ")[1].split(" | ")

    winning_numbers = sorted(int(num) for num in all_numbers[0].split())
    my_numbers = sorted(int(num) for num in all_numbers[1].split())

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

    if matched != 0:
        sum += 2 ** (matched - 1)

print(sum)
