lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

row_idxs = []
col_idxs = []
dots_row = ''.join(["." for _ in range(m)])

for i in range(n):
    if lines[i] == dots_row:
        row_idxs.append(i)

for j in range(m):
    flag = True
    for i in range(n):
        if (lines[i][j] != "."):
            flag = False
            break

    if flag:
        col_idxs.append(j)

for line in lines:
    print(line)

print()
# expand rows
for i, idx in enumerate(row_idxs):
    # adding i because there's shift in indexes with each row added
    lines.insert(idx+i, dots_row)

# new num of rows
n = len(lines)

# expand cols
for j, idx in enumerate(col_idxs):

    for i in range(n):
        lines[i] = lines[i][:idx+j+1] + "." + lines[i][idx+j+1:]

# new num of cols
m = len(lines[0])

for line in lines:
    print(line)

galaxies = []
for i in range(n):
    for j in range(m):
        if lines[i][j] == "#":
            galaxies.append((i, j))

sum = 0

for i in range(len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        sum += abs(galaxies[i][0] - galaxies[j][0]) + \
            abs(galaxies[i][1] - galaxies[j][1])

print(sum)

# part 1 ans - 9556712
