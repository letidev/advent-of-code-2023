import sys
import re

sys.setrecursionlimit(100000)

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

x = -1
y = -1

allowed = {
    "-": "lr",
    "|": "ud",
    "L": "ur",
    "J": "ul",
    "7": "ld",
    "F": "rd",
    ".": ""
}

opposites = {
    "d": "u",
    "u": "d",
    "l": "r",
    "r": "l"
}

dist = []
line_len = len(lines[0])

for i in range(len(lines)):
    dist.append([])
    dist[-1] = [0 for _ in range(len(lines[i]))]

    j = lines[i].find("S")

    if (j != -1):
        x = i
        y = j


def search(i, j, d, prev_dir):
    global allowed
    global opposites
    global dist
    global lines
    global line_len

    if (i < 0 or j < 0 or i >= len(lines) or j >= line_len):
        return

    if (lines[i][j] == "."):
        return

    if (lines[i][j] == "S" and d != 0):
        return

    if (lines[i][j] != "S" and allowed[lines[i][j]].find(opposites[prev_dir]) == -1):
        return

    if (dist[i][j] != 0 and dist[i][j] < d):
        return

    if (dist[i][j] == 0 or (dist[i][j] != 0 and dist[i][j] > d)):
        dist[i][j] = d

    # go up
    if (lines[i][j] == "S" or allowed[lines[i][j]].find("u") != -1) and prev_dir != "d":
        search(i-1, j, d+1, "u")

    # go down
    if (lines[i][j] == "S" or allowed[lines[i][j]].find("d") != -1) and prev_dir != "u":
        search(i+1, j, d+1, "d")

    # go left
    if (lines[i][j] == "S" or allowed[lines[i][j]].find("l") != -1) and prev_dir != "r":
        search(i, j-1, d+1, "l")

    # go right
    if (lines[i][j] == "S" or allowed[lines[i][j]].find("r") != -1) and prev_dir != "l":
        search(i, j+1, d+1, "r")

    return


# part 1
search(x, y, 0, "")

# split strings to lists of chars for easier work
for i in range(len(lines)):
    lines[i] = [x for x in lines[i]]

mx = 0
for i, line in enumerate(dist):
    # answer for part 1
    mx = max(mx, max(line))
    for j, _ in enumerate(line):
        # replaced junk pipes with dots
        if (dist[i][j] == 0 and lines[i][j] != "S"):
            lines[i][j] = "."


print()
print(mx)

# replace character with what S should be for part 2
lines[x][y] = "-"
inside = 0

# part 2
for i in range(len(lines)):
    walls = 0
    prev = ""

    for j in range(len(lines[i])):
        ch = lines[i][j]

        # junk pipes have been replaced with "."
        if (lines[i][j] == "."):
            if (walls % 2 == 1):
                inside += 1
                continue
            else:
                continue

        # horizontal is not wall, do nothing
        if (ch == "-"):
            continue

        elif (ch == "|"):
            walls += 1
            prev = ""

        elif (prev == ""):
            prev = ch

        else:
            if (prev == "L" and ch == "7"):
                walls += 1
            elif (prev == "F" and ch == "J"):
                walls += 1
            prev = ""

print(inside)
