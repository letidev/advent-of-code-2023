lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

row_idxs = []
col_idxs = []
dots_row = ''.join(["." for _ in range(m)])

# fidn empty rows
for i in range(n):
    if lines[i] == dots_row:
        row_idxs.append(i)

# find empty cols
for j in range(m):
    flag = True
    for i in range(n):
        if (lines[i][j] != "."):
            flag = False
            break

    if flag:
        col_idxs.append(j)

# list of all galaxies
galaxies = []
for i in range(n):
    for j in range(m):
        if lines[i][j] == "#":
            galaxies.append((i, j))

expansion = 999999
sum = 0

for i in range(len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]

        expanded_rows = 0
        expanded_cols = 0

        for row in row_idxs:
            if (row > g1[0] and row < g2[0]) or (row > g2[0] and row < g1[0]):
                expanded_rows += 1

        for col in col_idxs:
            if (col > g1[1] and col < g2[1]) or (col > g2[1] and col < g1[1]):
                expanded_cols += 1

        sum += (abs(galaxies[i][0] - galaxies[j][0]) + expanded_rows*expansion) + \
            (abs(galaxies[i][1] - galaxies[j][1]) + expanded_cols*expansion)

print(sum)

# part 1 ans - 9556712
# part 2 ans - 678626199476
