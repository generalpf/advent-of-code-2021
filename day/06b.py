import fileinput


original_fish = list(map(lambda i: int(i), fileinput.input().readline().rstrip().split(',')))
fish = {}
for age in range(0, 9):
    fish[age] = len(list(f for f in original_fish if f == age))

for day in range(256):
    # these will count down with the rest and start the next day at 8
    fish[9] = fish[0]
    for age in range(1, 10):
        fish[age - 1] = fish[age]
    # the 0s became 6s so add 'em in with the 7s that became 6s
    fish[6] += fish[9]
    print(f"after {day + 1} days we have {fish}")

print(fish[0] + fish[1] + fish[2] + fish[3] + fish[4] + fish[5] + fish[6] + fish[7] + fish[8])
