import fileinput


fish = list(map(lambda i: int(i), fileinput.input().readline().rstrip().split(',')))

for day in range(80):
    for i in range(len(fish) - 1, -1, -1):
        if fish[i] == 0:
            fish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1

print(len(fish))