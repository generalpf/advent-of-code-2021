import fileinput


polymer = ""
subs = {}

for next_line in fileinput.input():
    next_line = next_line.rstrip()
    if fileinput.isfirstline():
        polymer = next_line
    elif next_line == "":
        continue
    else:
        subst = next_line.split(' -> ')
        subs[subst[0]] = subst[1]

for step in range(10):
    i = 0
    while i < len(polymer) - 1:
        pair = polymer[i] + polymer[i + 1]
        if pair in subs:
            polymer = polymer[0:i + 1] + subs[pair] + polymer[i + 1:]
            i += 2
        else:
            i += 1
    print(f"step {step}: polymer {polymer}")

elements = {}

for e in polymer:
    if e in elements:
        elements[e] += 1
    else:
        elements[e] = 1

print(elements)
