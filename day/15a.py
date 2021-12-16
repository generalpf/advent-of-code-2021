import fileinput


grid = list(map(lambda line: list(map(lambda i: int(i), line.rstrip())), fileinput.input()))
lowest = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]

for y in range(len(grid) - 1, -1, -1):
    for x in range(len(grid[0]) - 1, -1, -1):
        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            lowest[y][x] = grid[y][x]
        elif x == len(grid[0]) - 1:
            lowest[y][x] = grid[y][x] + lowest[y + 1][x]
        elif y == len(grid) - 1:
            lowest[y][x] = grid[y][x] + lowest[y][x + 1]
        else:
            lowest[y][x] = grid[y][x] + min(lowest[y + 1][x], lowest[y][x + 1])

print(lowest[0][0] - grid[0][0])
