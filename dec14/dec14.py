lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

# an array of tuples (i, j) - the current position of a rock
rocks = []

# define all rocks in their original positions
for i in range(n):
    for j in range(m):
        if (lines[i][j] == "O"):
            rocks.append((i, j))


def roll_north():
    global rocks
    new_rock_positions = []

    for i in range(n):
        for j in range(m):

            if (i, j) in rocks:
                # if a rock is at the top row, it doesn't roll
                if i == 0:
                    new_rock_positions.append((i, j))

                else:
                    for row in reversed(range(i)):
                        # roll to 1 block under a solid rock
                        if lines[row][j] == "#" or (row, j) in new_rock_positions:
                            new_rock_positions.append((row+1, j))
                            break

                        # we've reached the top and haven't hit another
                        # round rock or a solid one
                        if row == 0:
                            new_rock_positions.append((row, j))

    rocks = new_rock_positions


def roll_west():
    global rocks
    new_rock_positions = []

    for j in range(m):
        for i in range(n):

            if (i, j) in rocks:
                if j == 0:
                    new_rock_positions.append((i, j))
                else:
                    for col in reversed(range(j)):
                        if lines[i][col] == "#" or (i, col) in new_rock_positions:
                            new_rock_positions.append((i, col+1))
                            break

                        if col == 0:
                            new_rock_positions.append((i, col))

    rocks = new_rock_positions


def roll_south():
    global rocks
    new_rock_positions = []

    for i in reversed(range(n)):
        for j in range(m):

            if (i, j) in rocks:
                if i == n - 1:
                    new_rock_positions.append((i, j))
                else:
                    for row in range(i+1, n):
                        if lines[row][j] == "#" or (row, j) in new_rock_positions:
                            new_rock_positions.append((row-1, j))
                            break

                        if row == n - 1:
                            new_rock_positions.append((row, j))

    rocks = new_rock_positions


def roll_east():
    global rocks
    new_rock_positions = []

    for j in reversed(range(m)):
        for i in range(n):

            if (i, j) in rocks:
                if j == m - 1:
                    new_rock_positions.append((i, j))
                else:
                    for col in range(j+1, m):
                        if lines[i][col] == "#" or (i, col) in new_rock_positions:
                            new_rock_positions.append((i, col-1))
                            break

                        if col == m - 1:
                            new_rock_positions.append((i, col))

    rocks = new_rock_positions


memo = {}
ans = 0

cycles = 1000000000
loop_start = 0
loop_size = 0
flag = False

for i in range(1, cycles + 1):
    roll_north()
    roll_west()
    roll_south()
    roll_east()

    rocks = sorted(rocks)

    if rocks not in memo.values():
        memo[i] = rocks
    else:
        for key, value in memo.items():
            if value == rocks:
                loop_start = key
                loop_size = i - key
                print("position at " + str(i) +
                      " is the same as position at " + str(key))
                flag = True
                break

    if flag:
        break

loop_to_calc = (loop_start-1) + (cycles - loop_start + 1) % loop_size
rocks_configuration = memo[loop_to_calc]

sum = 0
for rock in rocks_configuration:
    sum += n - rock[0]

print("loop start is - ", loop_start)  # 96
print("loop size is - ", loop_size)  # 78
print(sum)
