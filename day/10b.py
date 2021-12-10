import fileinput


incomplete_points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

incompletes = []

for next_line in fileinput.input():
    chars = list(next_line.rstrip())
    print(chars)
    stack = []
    for char in chars:
        if char in ['<', '(', '{', '[']:
            stack.append(char)
        elif char == '>' and stack.pop() != '<':
            stack.clear()
            break
        elif char == ')' and stack.pop() != '(':
            stack.clear()
            break
        elif char == '}' and stack.pop() != '{':
            stack.clear()
            break
        elif char == ']' and stack.pop() != '[':
            stack.clear()
            break
    if len(stack) > 1:
        points = 0
        while len(stack) > 0:
            char = stack.pop()
            points *= 5
            points += incomplete_points[char]
        incompletes.append(points)

incompletes.sort()

print(incompletes[int(len(incompletes) / 2)])
