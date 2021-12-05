import fileinput

zeroes = []
ones = []

for next_line in fileinput.input():
    next_line = next_line.rstrip()
    if fileinput.isfirstline():
        zeroes = [0] * len(next_line)
        ones = [0] * len(next_line)
    for i in range(len(next_line)):
        if next_line[i] == '0':
            zeroes[i] += 1
        else:
            ones[i] += 1
    print(f"{next_line} -> zeroes = {zeroes}, ones = {ones}")

gamma = ""
epsilon = ""

for i in range(len(zeroes)):
    if zeroes[i] > ones[i]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(f"gamma = {gamma}, epsilon = {epsilon}")

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(f"gamma = {gamma}, epsilon = {epsilon}, power = {gamma * epsilon}")
