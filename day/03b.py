import fileinput


def filter_most_common(readings: list, position: int) -> list:
    bit_we_want = most_common(readings, position)
    return list(filter(lambda r: int(r[position]) == bit_we_want, readings))


def filter_least_common(readings: list, position: int) -> list:
    bit_we_dont_want = most_common(readings, position)
    return list(filter(lambda r: int(r[position]) != bit_we_dont_want, readings))


def most_common(readings: list, position: int) -> int:
    zeroes = len(list(r for r in readings if r[position] == '0'))
    ones = len(readings) - zeroes
    if zeroes <= ones:
        return 1
    else:
        return 0
    

readings = []

for next_line in fileinput.input():
    readings.append(next_line.rstrip())

oxygen_candidates = readings
co2_candidates = readings

for i in range(len(readings[0])):
    if len(oxygen_candidates) > 1:
        oxygen_candidates = filter_most_common(oxygen_candidates, i)
    if len(co2_candidates) > 1:
        co2_candidates = filter_least_common(co2_candidates, i)
    print(f"bit {i}, oxygen cand = {oxygen_candidates}, co2 cand = {co2_candidates}")

oxygen = int(oxygen_candidates[0], 2)
co2 = int(co2_candidates[0], 2)
print(f"oxygen = {oxygen}, co2 = {co2}, life support = {oxygen * co2}")
