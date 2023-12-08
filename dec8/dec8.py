lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

network = {}

directions = lines[0]

for i in range(2, len(lines)):
    node = lines[i][0:3]
    left = lines[i][7:10]
    right = lines[i][12:15]

    network[node] = (left, right)

current_node = "AAA"
steps = 0
i = 0

while current_node != "ZZZ":
    if i == len(directions):
        i = 0

    dir = directions[i]
    current_node = network[current_node][0] if dir == "L" else network[current_node][1]
    # print(current_node)
    steps += 1
    i += 1

print(steps)
