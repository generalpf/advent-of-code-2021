import fileinput


dumbos = []

for next_line in fileinput.input():
    dumbos.append(list(map(lambda c: int(c), list(next_line.rstrip()))))


def add(y: int, x: int) -> int:
    dumbos[y][x] += 1
    if dumbos[y][x] == 10:
        return flash(y = y, x = x)
    return 0


def flash(y: int, x: int) -> int:
    f = 1
    if y > 0:
        if x > 0:
            f += add(y = y - 1, x = x - 1)
        f += add(y = y - 1, x = x)
        if x < 9:
            f += add(y = y - 1, x = x + 1)
    if x > 0:
        f += add(y = y, x = x - 1)
    if x < 9:
        f += add(y = y, x = x + 1)
    if y < 9:
        if x > 0:
            f += add(y = y + 1, x = x - 1)
        f += add(y = y + 1, x = x)
        if x < 9:
            f += add(y = y + 1, x = x + 1)
    return f


flashes = 0

for step in range(100):
    for y in range(10):
        for x in range(10):
            flashes += add(y = y, x = x)

    for y in range(10):
        for x in range(10):
            if dumbos[y][x] > 9:
                dumbos[y][x] = 0

print(flashes)