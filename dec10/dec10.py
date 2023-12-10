import sys

sys.setrecursionlimit(100000)

lines = []
with open("example3.txt") as f:
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


search(x, y, 0, "")

for line in lines:
    print(line)

print()

for line in dist:
    print(line)

mx = 0
for line in dist:
    mx = max(mx, max(line))

print()
print(mx)
