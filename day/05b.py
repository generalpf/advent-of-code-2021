import fileinput

grid = zeros = [[0 for _ in range(1000)] for _ in range(1000)]

for next_line in fileinput.input():
    coords = next_line.rstrip().split(' -> ')
    (startx, starty) = list(map(lambda i: int(i), coords[0].split(',')))
    (endx, endy) = list(map(lambda i: int(i), coords[1].split(',')))
    print(f"from ({startx},{starty}) to ({endx,endy})")
    if startx == endx:
        sign = 1 if endy > starty else -1
        for i in range(starty, endy + sign, sign):
            grid[i][startx] += 1
    elif starty == endy:
        sign = 1 if endx > startx else -1
        for i in range(startx, endx + sign, sign):
            grid[starty][i] += 1
    else:
        xsign = 1 if endx > startx else -1
        ysign = 1 if endy > starty else -1
        x = startx
        y = starty
        while x != endx:
            grid[y][x] += 1
            x += xsign
            y += ysign
        grid[y][x] += 1

overlaps = 0
for i in range(len(grid[0])):
    for j in range(len(grid)):
        if grid[i][j] > 1:
            overlaps += 1

print(f"overlaps = {overlaps}")
