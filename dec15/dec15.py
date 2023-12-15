input = ""
with open("test.txt") as f:
    input = f.read().splitlines()[0]

input = input.split(",")


def hash(seq: str):
    hash_value = 0
    for c in seq:
        hash_value = ((hash_value + ord(c)) * 17) % 256

    return hash_value


boxes = {}

for seq in input:
    label = ""
    focal = 0
    action = ""
    if "=" in seq:
        action = "="
        label = seq.split("=")[0]
        focal = seq.split("=")[1]
    else:
        action = "-"
        label = seq.split("-")[0]
        focal = -1

    box = hash(label)

    if box in boxes:
        ind = [x for x, y in enumerate(boxes[box]) if y[0] == label]

        if len(ind) == 1:
            if action == "=":
                boxes[box][ind[0]] = (label, focal)
            else:
                boxes[box].pop(ind[0])
        elif len(ind) == 0 and action == "=":
            boxes[box].append((label, focal))

    else:
        if action == "=":
            boxes[box] = []
            boxes[box].append((label, focal))

sum = 0
for box_num, box in boxes.items():
    for slot, lens in enumerate(box):
        sum += (box_num + 1) * (slot + 1) * int(lens[1])

print(sum)
