import re
import sys

sys.setrecursionlimit(1000000)

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()


def check_pattern(pattern, nums):
    springs = re.findall(r'#+', ''.join(pattern))

    if (len(springs) != len(nums)):
        return False

    for i in range(len(springs)):
        if (len(springs[i]) != nums[i]):
            return False

    return True


def generate(pattern, nums, generated, idx):
    if (idx == len(pattern)):
        if check_pattern(generated, nums):
            return 1
        else:
            return 0
    sum = 0

    if (pattern[idx] != "?"):
        sum += generate(pattern, nums, generated, idx+1)
    else:
        generated[idx] = "."
        sum += generate(pattern, nums, generated, idx+1)
        generated[idx] = "?"

        generated[idx] = "#"
        sum += generate(pattern, nums, generated, idx+1)
        generated[idx] = "?"

    return sum


sum = 0
for line in lines:
    spl = line.split(' ')

    pattern = [x for x in spl[0]]
    nums = [int(x) for x in spl[1].split(',')]

    list = re.findall(r'#+', ''.join(pattern))
    sum += generate(pattern, nums, pattern, 0)

print(sum)
