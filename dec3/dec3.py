
import re

lines = []

with open("test.txt") as f:
    lines = f.read().splitlines()

sum = 0


def is_adjacent_symbol(str, i, j):
    if (str[i][j] < '0' or str[i][j] > '9') and str[i][j] != '.':
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
                if is_adjacent_symbol(lines, i-1, j):  # above
                    flag = True
                    break

                if j < len(lines[i-1]) - 1:  # top right diagonal
                    if is_adjacent_symbol(lines, i-1, j+1):
                        flag = True
                        break

                if j > 0:  # top left diagonal
                    if is_adjacent_symbol(lines, i-1, j-1):
                        flag = True
                        break

            if j < (len(lines[i]) - 1):  # same line right
                if is_adjacent_symbol(lines, i, j+1):
                    flag = True
                    break

            if j > 0:  # same line left
                if is_adjacent_symbol(lines, i, j-1):
                    flag = True
                    break

            if i < len(lines) - 1:  # bottom row
                if is_adjacent_symbol(lines, i + 1, j):
                    flag = True
                    break

                if j < len(lines[i+1]) - 1:  # bottom right diagonal
                    if is_adjacent_symbol(lines, i+1, j+1):
                        flag = True
                        break

                if j > 0:  # bottom left diagonal
                    if is_adjacent_symbol(lines, i+1, j-1):
                        flag = True
                        break

        if flag:
            sum += int(number)

print(sum)
