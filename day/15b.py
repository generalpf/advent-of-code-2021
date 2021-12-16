import fileinput
from math import inf


grid_piece = list(map(lambda line: list(map(lambda i: int(i), line.rstrip())), fileinput.input()))
grid = [[None for _ in range(len(grid_piece[0]) * 5)] for _ in range(len(grid_piece) * 5)]
lowest = [[inf for _ in range(len(grid[0]))] for _ in range(len(grid))]

for piece_x in range(0, 5):
    for piece_y in range(0, 5):
        for x in range(len(grid_piece[0])):
            for y in range(len(grid_piece)):
                new_value = grid_piece[y][x] + piece_x + piece_y
                if new_value > 9:
                    new_value -= 9
                grid[piece_y * len(grid_piece) + y][piece_x * len(grid_piece[0]) + x] = new_value

lowest[0][0] = 0
visits = [(0, 0)]

while len(visits) > 0:
    (x, y) = visits.pop(0)
    if x > 0 and lowest[y][x - 1] > lowest[y][x] + grid[y][x - 1]:
        lowest[y][x - 1] = lowest[y][x] + grid[y][x - 1]
        visits.append((x - 1, y))
    if x < len(lowest[0]) - 1 and lowest[y][x + 1] > lowest[y][x] + grid[y][x + 1]:
        lowest[y][x + 1] = lowest[y][x] + grid[y][x + 1]
        visits.append((x + 1, y))
    if y > 0 and lowest[y - 1][x] > lowest[y][x] + grid[y - 1][x]:
        lowest[y - 1][x] = lowest[y][x] + grid[y - 1][x]
        visits.append((x, y - 1))
    if y < len(lowest) - 1 and lowest[y + 1][x] > lowest[y][x] + grid[y + 1][x]:
        lowest[y + 1][x] = lowest[y][x] + grid[y + 1][x]
        visits.append((x, y + 1))

print(lowest[len(lowest) - 1][len(lowest[0]) - 1])
