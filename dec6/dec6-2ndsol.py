import math

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

time = int(''.join(lines[0].split(":")[1].split()))
distance = int(''.join(lines[1].split(":")[1].split()))
D = math.sqrt(time**2 - 4*distance)

x1 = (- time + D) / (-2)
x2 = (- time - D) / (-2)

x1 = math.ceil(x1)
x2 = math.floor(x2)

print(x2 - x1 + 1)
