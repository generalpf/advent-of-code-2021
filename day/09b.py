import fileinput


heightmap = []

for next_line in fileinput.input():
    heightmap.append(list(map(lambda c: int(c), list(next_line.rstrip()))))


def basin_size(y: int, x: int) -> int:
    size = 1
    heightmap[y][x] = 9
    if y > 0 and heightmap[y - 1][x] != 9:
        size += basin_size(y - 1, x)
    if y < len(heightmap) - 1 and heightmap[y + 1][x] != 9:
        size += basin_size(y + 1, x)
    if x > 0 and heightmap[y][x - 1] != 9:
        size += basin_size(y, x - 1)
    if x < len(heightmap[0]) - 1 and heightmap[y][x + 1] != 9:
        size += basin_size(y, x + 1)
    return size


basins = []

for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        if heightmap[y][x] == 9:
            continue
        # we are starting a new basin
        basins.append(basin_size(y, x))

basins = sorted(basins, reverse=True)
print(basins[0] * basins[1] * basins[2])