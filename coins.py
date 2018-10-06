results = {1: 1, 2: 2, 3: 2}
for i in range(4, 101):
    flips = 2
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            flips += 1
    results[i] = flips
odds = [r for r in results if results[r] % 2 == 1]
print(odds)

from random import randrange
results = {}
for i in range(1, 49):
    percent = min(100, int(i / 48. * 100))
    print(u"\u2588" * percent + u"\u2592" * (100 - percent), str(percent) + '%', end = '\r')
    for j in range(i + 1, 50):
        for k in range(j + 1, 51):
            live = 0
            die = 0
            for tries in range(200):
                space = 0
                while space < k:
                    roll = randrange(1, 7)
                    space += roll
                    if space in (i, j, k):
                        live += 1
                        break
                else:
                    die += 1
            results[(i, j, k)] = live / float(live + die)
print()
print(max(results, key = lambda result: results[result]))
result_pairs = results.items()
sorted_pairs = sorted(result_pairs, key = lambda pair: pair[1])
for combo, result in sorted_pairs[-10:]:
    print(combo, result)
