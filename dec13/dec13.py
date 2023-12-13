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


for grid in grids:
    n = len(grid)  # rows
    m = len(grid[0])  # cols

    # search for horizontal match:
    for i in range(n - 1):
        if grid[i] == grid[i+1]:
            up = i-1
            down = i+2
            pefrect_match = True

            while up >= 0 and down < n:
                if (grid[up] != grid[down]):
                    pefrect_match = False
                    break

                up -= 1
                down += 1

            if pefrect_match:
                sum += (i + 1) * 100

    # search for vertical match:
    for j in range(m - 1):
        if columns_match(grid, j, j+1):
            left = j-1
            right = j+2
            pefrect_match = True

            while left >= 0 and right < m:
                if not columns_match(grid, left, right):
                    pefrect_match = False
                    break

                left -= 1
                right += 1

            if pefrect_match:
                sum += j + 1

print(sum)
