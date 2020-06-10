def card_shuffle(cards):
    left, right = divide(cards)
    new_cards = merge(left, right)

    return new_cards


def merge(left, right):
    llen = len(left)
    rlen = len(right)
    index = 0

    new_cards = []
    while index < rlen and index < llen:
        new_cards.append(right[index])
        new_cards.append(left[index])
        index += 1

    if index < rlen:
        new_cards.append(right[-1])
    return new_cards


def divide(cards):
    mid = int(len(cards) / 2)
    left = cards[:mid]
    right = cards[mid:]
    return left, right


cards = list(range(1, 55))
print("Begin to shuffle:", cards)

new_cards = []
count = 0
while cards != new_cards:
    if count == 0:
        new_cards = cards
    new_cards = card_shuffle(new_cards)
    count += 1
    print("Loop ", count, ":", new_cards)


print("After {0} loops, the cards return to the initial state.".format(count))

