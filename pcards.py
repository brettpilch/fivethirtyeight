from collections import Counter
import random

def name_hand(dice):
    hand = Counter(dice).most_common()
    return tuple(die[1] for die in hand)

def name_hand2(dice):
    hand = sorted(dice)
    return tuple(hand)

def simulate(n = 100000, dice = 6, faces = 6, name_func = name_hand):
    table = Counter()
    for i in range(n):
        hand = [random.randrange(faces) for die in range(dice)]
        table[name_func(hand)] += 1
        # for j in range(faces):
        #     if hand.count(j) == 1:
        #         table[j] += 1
        # table['sum: ' + str(sum(hand))] += 1
    return Counter({key: value / float(n) for key, value in table.items()}).most_common()

print(simulate(100000, 2, 6, name_func = name_hand2))