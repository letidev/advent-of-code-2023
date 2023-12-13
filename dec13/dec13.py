lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

grids = [[]]
for line in lines:
    if line == "":
        grids.append([])
    else:
        grids[-1].append(line)

sum = 0


def columns_match(grid, left, right):
    for i in range(len(grid)):
        if grid[i][left] != grid[i][right]:
            return False

    return True


def flip(type):
    return "#" if type == "." else "."


def has_horizontal_smudge(up, down):
    smudges = []

    for i in range(len(up)):
        if up[i] != down[i]:
            smudges.append(i)

    return False if len(smudges) != 1 else True


def has_vertical_smudge(grid, left, right):
    smudges = []

    for i in range(len(grid)):
        if grid[i][left] != grid[i][right]:
            smudges.append(i)

    return False if len(smudges) != 1 else True


def print_grid(grid):
    for line in grid:
        print(line)
    print()


for grid in grids:
    n = len(grid)  # rows
    m = len(grid[0])  # cols

    # print_grid(grid)

    ### FIX LINE SMUDGE AND SUM ###
    for i in range(n - 1):
        up = i
        down = i+1
        has_smudge = False
        match = True

        while up >= 0 and down < n:
            if not has_smudge and has_horizontal_smudge(grid[up], grid[down]):
                has_smudge = True

            elif grid[up] != grid[down]:
                match = False
                break

            up -= 1
            down += 1

        if has_smudge and match:
            sum += (i+1) * 100
            break

    ### FIX COLUMN SMUDGE AND SUM ###
    for j in range(m - 1):
        left = j
        right = j + 1
        has_smudge = False
        match = True

        while left >= 0 and right < m:
            if not has_smudge and has_vertical_smudge(grid, left, right):
                has_smudge = True
            elif not columns_match(grid, left, right):
                match = False
                break

            left -= 1
            right += 1

        if has_smudge and match:
            sum += j + 1
            break

print(sum)
