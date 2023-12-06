import math

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

time = int(''.join(lines[0].split(":")[1].split()))
distance = int(''.join(lines[1].split(":")[1].split()))

print(time)
print(distance)

left = 0
right = math.ceil(time / 2)
found = -1

while True:
    mid = math.ceil((left + right) / 2)
    dist = mid*time - mid**2

    if dist <= distance:
        left = mid
    else:
        if mid - 1 >= left and (mid-1)*time - (mid-1)**2 <= distance:
            found = mid
            break
        else:
            right = mid

margin = time - 2 * found + 1

print(margin)
