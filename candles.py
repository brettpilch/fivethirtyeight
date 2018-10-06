from functools import lru_cache
import random

@lru_cache()
def blows_left(candles):
    if candles == 0:
        return 0
    else:
        return 1 + sum(blows_left(i) for i in range(candles)) / candles

# print(blows_left(30))

def rolls_to_cash(sides):
    roll = random.randrange(sides)
    next_roll = random.randrange(sides)
    cash = 2
    while next_roll >= roll:
        roll, next_roll = next_roll, random.randrange(sides)
        cash += 1
    return cash

def expected_cash(sides, n):
    total = 0
    for i in range(n):
        total += rolls_to_cash(sides)
    return total / float(n)

# print(expected_cash(1000000, 1000000))
