import sys

file1 = open('test.txt', 'r')
lines = file1.readlines()

sum = 0

num_map = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 0,
}

sum = 0
for line in lines:

    min_ind = sys.maxsize
    first_digit = 0
    for key in num_map:
        current_ind = line.find(key)

        if (current_ind < min_ind and current_ind != -1):
            min_ind = current_ind
            first_digit = num_map[key]

    max_ind = -1
    second_digit = 0
    for key in num_map:
        current_ind = line.rfind(key)

        if (current_ind > max_ind and current_ind != -1):
            max_ind = current_ind
            second_digit = num_map[key]

    sum += (first_digit * 10 + second_digit)

print(sum)
