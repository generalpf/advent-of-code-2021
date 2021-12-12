import fileinput


dumbos = []

for next_line in fileinput.input():
    dumbos.append(list(map(lambda c: int(c), list(next_line.rstrip()))))


def add(y: int, x: int):
    dumbos[y][x] += 1
    if dumbos[y][x] == 10:
        flash(y = y, x = x)


def flash(y: int, x: int):
    if y > 0:
        if x > 0:
            add(y = y - 1, x = x - 1)
        add(y = y - 1, x = x)
        if x < 9:
            add(y = y - 1, x = x + 1)
    if x > 0:
        add(y = y, x = x - 1)
    if x < 9:
        add(y = y, x = x + 1)
    if y < 9:
        if x > 0:
            add(y = y + 1, x = x - 1)
        add(y = y + 1, x = x)
        if x < 9:
            add(y = y + 1, x = x + 1)


step = 1

while True:
    for y in range(10):
        for x in range(10):
            add(y = y, x = x)

    flashes = 0
    for y in range(10):
        for x in range(10):
            if dumbos[y][x] > 9:
                dumbos[y][x] = 0
                flashes += 1

    if flashes == 100:
        print(f"they all flashed on step {step}")
        exit(0)

    step += 1
