import fileinput
from collections import deque


def mark_off(cards: list, call: int) -> list:
    return list(map(lambda card: list(map(lambda row: list(map(lambda num: 0 if num == call else num, row)), card)), cards))


def did_card_win(card: list) -> bool:
    # check rows
    for i in range(5):
        if card[i][0] + card[i][1] + card[i][2] + card[i][3] + card[i][4] == 0:
            return True
    # check columns
    for i in range(5):
        if card[0][i] + card[1][i] + card[2][i] + card[3][i] + card[4][i] == 0:
            return True
    return False


def card_score(card: list, call: int) -> int:
    sum = 0
    for i in range(5):
        for j in range(5):
            sum += card[i][j]
    return sum * call


inputter = fileinput.input()

calls = deque(list(map(lambda d: int(d), inputter.readline().rstrip().split(','))))
print(f"calls = {calls}")

cards = []

while True:
    if inputter.readline() == '':
        break

    new_card = []
    for i in range(5):
        new_card.append(list(map(lambda d: int(d), inputter.readline().strip().replace('  ', ' ').split(' '))))
    cards.append(new_card)

while len(calls) > 0:
    call = calls.popleft()
    cards = mark_off(cards, call)
    for card in cards:
        if did_card_win(card):
            score = card_score(card, call)
            print(f"score = {score}")
            exit(0)
