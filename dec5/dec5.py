import sys

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

seeds_map = []
maps = []

flag = -1


def add_map(line, ind):
    global maps

    if (line.strip() and line[0].isnumeric()):
        split_line = [int(x) for x in line.split()]

        if len(maps) < ind + 1:
            maps.append([])

        # the source and dest are reversed
        maps[ind].append((split_line[1], split_line[0], split_line[2]))


for line in lines:
    if line.startswith("seeds:"):
        seeds = [int(x) for x in line.split(":")[1].split()]
        for i in range(0, len(seeds), 2):
            seeds_map.append((seeds[i], seeds[i + 1]))

    if line.startswith("seed-to-soil"):
        flag = 0
    if line.startswith("soil-to-fertilizer"):
        flag = 1
    if line.startswith("fertilizer-to-water"):
        flag = 2
    if line.startswith("water-to-light"):
        flag = 3
    if line.startswith("light-to-temperature"):
        flag = 4
    if line.startswith("temperature-to-humidity"):
        flag = 5
    if line.startswith("humidity-to-location"):
        flag = 6

    add_map(line, flag)

min_location = sys.maxsize
maps.reverse()

num = 0
flag = False

while not flag:
    mapped = num
    for i in range(len(maps)):  # all maps of e certain type
        for map in maps[i]:  # a single mapping row
            dest, source, range_sz = map
            if mapped >= source and mapped < source + range_sz:
                mapped = mapped - source + dest
                break

    # we've gone through all maps from location to seed

    # now check if seed number is in given seeds
    for seed_map in seeds_map:
        seed_start, range_sz = seed_map
        if mapped >= seed_start and mapped < seed_start + range_sz:
            min_location = num
            flag = True

    num += 1

print(min_location)
