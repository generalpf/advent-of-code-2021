def blank_paper(width: int, height: int) -> list:
    return list(list(0 for _ in range(width)) for _ in range(height))


with open("day/data/13.real.txt", "r") as f:
    lines = f.readlines()

largest_x = 0
largest_y = 0

for next_line in lines:
    if next_line.rstrip() == "":
        break
    coord = list(map(lambda i: int(i), next_line.rstrip().split(",")))
    if coord[0] > largest_x:
        largest_x = coord[0]
    if coord[1] > largest_y:
        largest_y = coord[1]

paper = blank_paper(width = largest_x + 1, height = largest_y + 1)
print(f"paper is {len(paper[0])}x{len(paper)}")
    
i = 0
while True:
    next_line = lines[i].rstrip()
    if next_line == "":
        i += 1
        break
    coord = list(map(lambda i: int(i), next_line.split(",")))
    paper[coord[1]][coord[0]] = 1
    i += 1

while i < len(lines):
    next_line = lines[i].rstrip()
    parts = next_line.split(" ")[2].split("=")
    if parts[0] == "y":
        new_height = len(paper) - int(parts[1]) - 1
        new_paper = blank_paper(width = len(paper[0]), height = new_height)
        for y in range(len(paper)):
            for x in range(len(paper[0])):
                if y < new_height:
                    new_paper[y][x] = paper[y][x]
                elif y > new_height:
                    new_paper[len(paper) - y - 1][x] += paper[y][x]
        paper = new_paper
    elif parts[0] == "x":
        new_width = len(paper[0]) - int(parts[1]) - 1
        new_paper = blank_paper(width = new_width, height = len(paper))
        for y in range(len(paper)):
            for x in range(len(paper[0])):
                if x < new_width:
                    new_paper[y][x] = paper[y][x]
                elif x > new_width:
                    new_paper[y][len(paper[0]) - x - 1] += paper[y][x]
        paper = new_paper
    print(f"paper is now {len(paper[0])}x{len(paper)}")
    i += 1

dots = 0
for y in range(len(paper)):
    for x in range(len(paper[0])):
        print("#" if paper[y][x] > 0 else ".", end="")
    print("\n")
