import math

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

network = {}

directions = lines[0]

starting_nodes = []
steps_to_z = []

for i in range(2, len(lines)):
    node = lines[i][0:3]
    left = lines[i][7:10]
    right = lines[i][12:15]

    network[node] = (left, right)
    starting_nodes.append(node) if node[2] == "A" else starting_nodes

print(starting_nodes)

for i in range(len(starting_nodes)):
    current_node = starting_nodes[i]
    steps = 0
    i = 0

    while current_node[2] != "Z":
        if i == len(directions):
            i = 0

        dir = directions[i]
        current_node = network[current_node][0] if dir == "L" else network[current_node][1]
        steps += 1
        i += 1

    steps_to_z.append(steps)

total_steps = steps_to_z[0]

for i in range(1, len(steps_to_z)):
    total_steps = math.lcm(total_steps, steps_to_z[i])

print(steps_to_z)
print(total_steps)
