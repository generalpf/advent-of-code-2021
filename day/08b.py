import fileinput


sum = 0

for next_line in fileinput.input():
    parts = next_line.rstrip().split(' | ')
    inputs = list(map(lambda i: set(i), parts[0].split(' ')))
    outputs = list(map(lambda i: set(i), parts[1].split(' ')))

    # digits[i] is the index into inputs for the `i` digit
    digits = list(map(lambda i: None, range(10)))

    for i in range(10):
        if len(inputs[i]) == 3:
            digits[7] = i
        elif len(inputs[i]) == 2:
            digits[1] = i
        elif len(inputs[i]) == 7:
            digits[8] = i
        elif len(inputs[i]) == 4:
            digits[4] = i

    for i in range(10):
        if len(inputs[i]) == 5:
            # 2, 3, or 5
            # if it has the 7 inside it, this is the 3
            if len(inputs[i].intersection(inputs[digits[7]])) == 3:
                digits[3] = i
            # if it intersects with the 4 in 3 places, this is the 5
            elif len(inputs[i].intersection(inputs[digits[4]])) == 3:
                digits[5] = i
            # otherwise it's the 2
            else:
                digits[2] = i

    for i in range(10):
        if len(inputs[i]) == 6:
            # 0, 6, or 9
            # if it doesn't have the 1 inside it, this is the 6
            if len(inputs[i].intersection(inputs[digits[1]])) == 1:
                digits[6] = i
            # if it has the 5 inside it, it's the 9
            elif len(inputs[i].intersection(inputs[digits[5]])) == 5:
                digits[9] = i
            # otherwise it's the 0
            else:
                digits[0] = i

    output_array = [None, None, None, None]
    for i in range(4):
        for j in range(10):
            if inputs[digits[j]] == outputs[i]:
                output_array[i] = j
                break

    output = output_array[0] * 1000 + output_array[1] * 100 + output_array[2] * 10 + output_array[3]
    sum += output

print(sum)
