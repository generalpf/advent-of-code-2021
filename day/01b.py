import fileinput


sums = []
increases = 0

for next_line in fileinput.input():
    next_number = int(next_line)
    lineno = fileinput.lineno() - 1
    sums.append(next_number)
    if lineno > 0:
        sums[lineno - 1] += next_number
        if lineno > 1:
            sums[lineno - 2] += next_number
            if lineno > 2 and sums[lineno - 2] > sums[lineno - 3]:
                increases += 1

print(f"{increases} increases")