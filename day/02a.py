import fileinput


x = 0
z = 0

for next_line in fileinput.input():
    parts = next_line.split(' ')
    command = parts[0]
    magnitude = int(parts[1])
    if command == "forward":
        x += magnitude
    elif command == "down":
        z += magnitude
    elif command == "up":
        z -= magnitude

print(f"x = {x}, z = {z}, x * z = {x * z}")
