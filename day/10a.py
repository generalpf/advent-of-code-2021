import fileinput


points = 0

for next_line in fileinput.input():
    chars = list(next_line.rstrip())
    print(chars)
    stack = []
    for char in chars:
        if char in ['<', '(', '{', '[']:
            stack.append(char)
        elif char == '>' and stack.pop() != '<':
            points += 25137
            break
        elif char == ')' and stack.pop() != '(':
            points += 3
            break
        elif char == '}' and stack.pop() != '{':
            points += 1197
            break
        elif char == ']' and stack.pop() != '[':
            points += 57
            break

print(points)
