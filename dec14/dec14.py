lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

# (x1, y1): (x2: y2), where first tuple is old position
# the second tuple is the new position after rolling
rocks = {}

for i in range(n):
    for j in range(m):

        # rocks on 1st line don't roll
        if lines[i][j] == "O":
            if i == 0:
                rocks[(i, j)] = (i, j)

            else:
                for row in reversed(range(i)):
                    # roll to 1 block under a solid rock
                    if lines[row][j] == "#":
                        rocks[(i, j)] = (row+1, j)
                        break

                    # roll to 1 block under the new position of
                    # a discovered round rock
                    if lines[row][j] == "O":
                        moved_rock_new_pos = rocks[(row, j)]
                        rocks[(i, j)] = (moved_rock_new_pos[0]+1, j)
                        break

                    # the round rock hasn't hit neither a solid
                    # nor another round rock
                    if lines[row][j] == "." and row == 0:
                        rocks[(i, j)] = (0, j)

        # print(i, j)
        # print(rocks)
        # print()


sum = 0
for _, new_pos in rocks.items():
    sum += n - new_pos[0]

print(sum)
