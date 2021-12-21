import re
from math import ceil, floor
import fileinput

sample_1 = "[[[[[9,8],1],2],3],4]"
sample_2 = "[7,[6,[5,[4,[3,2]]]]]"
sample_3 = "[[6,[5,[4,[3,2]]]],1]"
sample_4 = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
sample_5 = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"


def explode_any(s: str) -> str:
    depth = 0
    for i in range(len(s)):
        if s[i] == "[":
            depth += 1
        elif s[i] == "]":
            depth -= 1
        elif s[i].isnumeric() and depth >= 5:
            m = re.match(r"^(\d+),(\d+)", s[i:])
            if m and len(m.groups()) == 2:
                left_number = int(m.group(1))
                right_number = int(m.group(2))
                # look left for number to increment
                j = i - 1
                left_index_first_digit = None
                left_index_last_digit = None
                while j > -1:
                    if s[j].isnumeric() and left_index_last_digit is None:
                        left_index_last_digit = j
                    elif not s[j].isnumeric() and left_index_last_digit:
                        left_index_first_digit = j + 1
                        break
                    j -= 1
                # look right for number to increment
                j = i + len(m.group(1)) + 1 + len(m.group(2))
                right_index_first_digit = None
                right_index_last_digit = None
                while j < len(s):
                    if s[j].isnumeric() and right_index_first_digit is None:
                        right_index_first_digit = j
                    elif not s[j].isnumeric() and right_index_first_digit:
                        right_index_last_digit = j - 1
                        break
                    j += 1
                # assemble the new string
                if left_index_first_digit:
                    lefter_number = int(s[left_index_first_digit:left_index_last_digit + 1])
                    result = f"{s[:left_index_first_digit]}{lefter_number + left_number}{s[left_index_last_digit + 1:i - 1]}"
                else:
                    result = s[:i - 1]
                result += "0"
                if right_index_last_digit:
                    righter_number = int(s[right_index_first_digit:right_index_last_digit + 1])
                    result += f"{s[i + len(m.group(1)) + 1 + len(m.group(2)) + 1:right_index_first_digit]}{righter_number + right_number}{s[right_index_last_digit + 1:]}"
                else:
                    result += s[i + len(m.group(1)) + 1 + len(m.group(2)) + 1:]
                return result

    return None


def split_any(s: str) -> str:
    m = re.search(r"(\d{2,})", s)
    if m:
        split_this = int(s[m.start(1):m.end(1)])
        left = int(floor(split_this / 2))
        right = int(ceil(split_this / 2))
        return f"{s[:m.start(1)]}[{left},{right}]{s[m.end(1):]}"

    return None


def add(f1: str, f2: str) -> str:
    sum = f"[{f1},{f2}]"
    while True:
        exploded = explode_any(sum)
        if not exploded:
            split = split_any(sum)
            if not split:
                return sum
            else:
                sum = split
        else:
            sum = exploded


def magnitude(s: str) -> int:
    # keep replacing pairs until we have one pair and that's it
    while True:
        m = re.search("(\d+),(\d+)", s)
        if m:
            left = int(m.group(1))
            right = int(m.group(2))
            magnitude = left * 3 + right * 2
            s = f"{s[:m.start(1) - 1]}{magnitude}{s[m.end(2) + 1:]}"
        else:
            return int(s)


sum = None

for next_line in fileinput.input():
    if fileinput.isfirstline():
        sum = next_line.rstrip()
    else:
        sum = add(sum, next_line.rstrip())

print(sum)
print(magnitude(sum))
