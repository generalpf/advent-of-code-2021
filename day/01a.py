import fileinput


prev_number = None
increments = 0
for next_line in fileinput.input():
	next_number = int(next_line)
	if prev_number != None and next_number > prev_number:
		increments += 1
	prev_number = next_number

print(f"there were {increments} increments")
