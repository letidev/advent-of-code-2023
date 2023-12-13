import time

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

memo = {}


def generate(pattern, nums):
    # reached end
    if pattern == "":
        # if no numbers to cover - all good
        if nums == ():
            return 1
        else:  # bad
            return 0

    # no numbers left to cover
    if nums == ():
        # if there are still broken left - bad
        if "#" in pattern:
            return 0
        else:  # good
            return 1

    sum = 0
    key = (pattern, nums)

    if key in memo:
        return memo[key]

    if pattern[0] in ".?":
        sum += generate(pattern[1:], nums)

    if pattern[0] in "#?":
        if nums[0] <= len(pattern) and "." not in pattern[:nums[0]] and (nums[0] == len(pattern) or pattern[nums[0]] != "#"):
            sum += generate(pattern[nums[0] + 1:], nums[1:])

    memo[key] = sum
    return sum


sum = 0

start_time = time.time()

for line in lines:
    pattern, nums = line.split()
    nums = tuple(map(int, nums.split(",")))

    pattern = "?".join([pattern] * 5)
    nums *= 5

    sum += generate(pattern, nums)
print("--- %s seconds --- " % (time.time() - start_time))
print(sum)
