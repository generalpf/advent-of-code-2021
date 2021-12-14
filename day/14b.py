import fileinput


def increment_map(map: map, key: str, by: int = 1):
    if key in map:
        map[key] += by
    else:
        map[key] = by


subs = {}
pairs = {}
elements = {}

for next_line in fileinput.input():
    next_line = next_line.rstrip()
    if fileinput.isfirstline():
        for e in next_line:
            increment_map(elements, e)
        for i in range(len(next_line) - 1):
            pair = next_line[i] + next_line[i + 1]
            increment_map(pairs, pair)
    elif next_line == "":
        continue
    else:
        subst = next_line.split(' -> ')
        subs[subst[0]] = subst[1]

for step in range(40):
    new_pairs = pairs.copy()
    for pair in pairs:
        if pair in subs:
            new_element = subs[pair]
            increment_map(elements, new_element, by = pairs[pair])
            increment_map(new_pairs, pair[0] + new_element, by = pairs[pair])
            increment_map(new_pairs, new_element + pair[1], by = pairs[pair])
            increment_map(new_pairs, pair, by = -pairs[pair])
    pairs = new_pairs


elements = dict(sorted(elements.items(), key=lambda e: e[1]))
print(elements)
