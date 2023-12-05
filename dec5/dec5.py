import sys

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

seeds = []
maps = []

flag = -1


def add_map(line, ind):
    global maps

    if (line.strip() and line[0].isnumeric()):
        split_line = [int(x) for x in line.split()]

        if len(maps) < ind + 1:
            maps.append([])

        maps[ind].append((split_line[0], split_line[1], split_line[2]))


for line in lines:
    if line.startswith("seeds:"):
        seeds = [int(x) for x in line.split(":")[1].split()]

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


for seed in seeds:
    mapped_num = seed

    for map_type in maps:  # all maps of a certain type
        for map in map_type:  # a single mapping row
            dest, source, range = map
            if mapped_num >= source and mapped_num < source + range:
                mapped_num = mapped_num - source + dest
                break

    min_location = mapped_num if mapped_num < min_location else min_location

print(min_location)
