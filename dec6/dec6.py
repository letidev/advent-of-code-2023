import math

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

times = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]

print(times)
print(distances)

prod = 1

for i in range(len(times)):
    left = 0
    right = math.ceil(times[i] / 2)
    found = -1

    while True:
        mid = math.ceil((left + right) / 2)
        dist = mid*times[i] - mid**2

        if dist <= distances[i]:
            left = mid
        else:
            if mid - 1 >= left and (mid-1)*times[i] - (mid-1)**2 <= distances[i]:
                found = mid
                break
            else:
                right = mid

    margin = times[i] - 2 * found + 1
    prod *= margin

print(prod)
