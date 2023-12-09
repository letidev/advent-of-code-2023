
lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

sum = 0

for line in lines:
    sequences = []

    initial_seq = [int(x) for x in line.split()]
    sequences.append(initial_seq)

    flag = False

    while not flag:
        zeroes = 0
        seq = []

        for i in range(len(sequences[-1]) - 1):
            num = sequences[-1][i+1] - sequences[-1][i]
            seq.append(num)

            zeroes = zeroes + 1 if num == 0 else zeroes

        sequences.append(seq)

        if zeroes == len(sequences[-1]):
            flag = True

    last = 0

    sequences.reverse()

    for seq in sequences:
        num = seq[-1] + num

    print(num)
    sum += num

print(sum)
