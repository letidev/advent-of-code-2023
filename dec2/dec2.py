
lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

sum = 0

for line in lines:
    semicolon_split = line.split(":")

    gameid = semicolon_split[0].split(' ')[1]

    game_draws = semicolon_split[1].split(';')

    max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for game_draw in game_draws:
        truncated = game_draw.strip()

        cube_types = truncated.split(", ")

        for cube_type in cube_types:
            splitted = cube_type.split(' ')
            count = int(splitted[0])
            colour = splitted[1]

            if count > max_cubes[colour]:
                max_cubes[colour] = count

    sum += (max_cubes["red"] * max_cubes["green"] * max_cubes["blue"])

print(sum)
