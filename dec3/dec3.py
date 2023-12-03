
import re

lines = []

with open("test.txt") as f:
    lines = f.read().splitlines()

sum = 0

gears_numbers = []


def add_number_to_gears_list(i, j, number):
    tuple = (i, j, number)
    gears_numbers.append(tuple)

    x = [item for item in gears_numbers if item[0] == i and item[1] == j]

    if (len(x) == 2):
        global sum
        sum += int(x[0][2]) * int(x[1][2])


def is_next_to_gear(str, i, j, number):
    if str[i][j] == "*":
        add_number_to_gears_list(i, j, number)
        return True

    return False


for i in range(len(lines)):
    numbers = re.findall(r'\b\d+\b', lines[i])

    search_pos = 0

    for number in numbers:
        num_start_pos = lines[i].find(number, search_pos)
        search_pos = num_start_pos + len(number)
        flag = False

        for j in range(num_start_pos, num_start_pos + len(number), 1):
            if i > 0:  # top row
                if is_next_to_gear(lines, i-1, j, number):  # above
                    flag = True
                    break

                if j < len(lines[i-1]) - 1:  # top right diagonal
                    if is_next_to_gear(lines, i-1, j+1, number):
                        flag = True
                        break

                if j > 0:  # top left diagonal
                    if is_next_to_gear(lines, i-1, j-1, number):
                        flag = True
                        break

            if j < (len(lines[i]) - 1):  # same line right
                if is_next_to_gear(lines, i, j+1, number):
                    flag = True
                    break

            if j > 0:  # same line left
                if is_next_to_gear(lines, i, j-1, number):
                    flag = True
                    break

            if i < len(lines) - 1:  # bottom row
                if is_next_to_gear(lines, i + 1, j, number):
                    flag = True
                    break

                if j < len(lines[i+1]) - 1:  # bottom right diagonal
                    if is_next_to_gear(lines, i+1, j+1, number):
                        flag = True
                        break

                if j > 0:  # bottom left diagonal
                    if is_next_to_gear(lines, i+1, j-1, number):
                        flag = True
                        break

print(sum)
