import fileinput


heightmap = []

for next_line in fileinput.input():
    heightmap.append(list(map(lambda c: int(c), list(next_line.rstrip()))))

total_risk = 0

for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        if y > 0 and heightmap[y][x] >= heightmap[y - 1][x]:
            continue
        if y < len(heightmap) - 1 and heightmap[y][x] >= heightmap[y + 1][x]:
            continue
        if x > 0 and heightmap[y][x] >= heightmap[y][x - 1]:
            continue
        if x < len(heightmap[0]) - 1 and heightmap[y][x] >= heightmap[y][x + 1]:
            continue
        print(f"({x},{y}) is a risk point")
        total_risk += heightmap[y][x] + 1

print(total_risk)