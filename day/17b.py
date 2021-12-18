# target area: x=20..30, y=-10..-5
sample_x = (20, 30)
sample_y = (-10, -5)

# target area: x=60..94, y=-171..-136
real_x = (60, 94)
real_y = (-171, -136)

target_x = real_x
target_y = real_y


def hits_target(vel_x: int, vel_y: int) -> bool:
    global target_x, target_y
    
    x = 0
    y = 0
    (min_x, max_x) = target_x
    (min_y, max_y) = target_y

    while x <= max_x and y >= min_y:
        x += vel_x
        y += vel_y
        vel_x = max(0, vel_x - 1)
        vel_y -= 1
        if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
            return True
    
    return False


hits = 0

for y in range(-400, 400):
    for x in range(400):
        if hits_target(vel_x = x, vel_y = y):
            hits += 1

print(hits)
