import fileinput


ones = 0
fours = 0
sevens = 0
eights = 0

for next_line in fileinput.input():
    parts = next_line.rstrip().split(' | ')
    inputs = parts[0].split(' ')
    outputs = parts[1].split(' ')
    ones += len(list(o for o in outputs if len(o) == 2))
    fours += len(list(o for o in outputs if len(o) == 4))
    sevens += len(list(o for o in outputs if len(o) == 3))
    eights += len(list(o for o in outputs if len(o) == 7))

print(f"1s = {ones}, 4s = {fours}, 7s = {sevens}, 8s = {eights}")
