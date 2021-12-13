import fileinput


graph = {}

for next_line in fileinput.input():
    edge = next_line.rstrip().split('-')
    if edge[0] not in graph.keys():
        graph[edge[0]] = [edge[1]]
    else:
        graph[edge[0]].append(edge[1])
    if edge[1] not in graph.keys():
        graph[edge[1]] = [edge[0]]
    else:
        graph[edge[1]].append(edge[0])


def paths_to_end(last: str, visited: list, debug_string: str) -> int:
    total = 0
    for x in graph[last]:
        if x == "start":
            continue
        elif x == "end":
            print(debug_string + x)
            total += 1
        elif x.islower() and x in visited:
            continue
        else:
            new_visited = visited.copy()
            if x.islower():
                new_visited.append(x)
            total += paths_to_end(x, new_visited, debug_string + x + ",")
    return total


paths = paths_to_end(last = "start", visited = [], debug_string="start,")
print(f"there are {paths} unique paths")
