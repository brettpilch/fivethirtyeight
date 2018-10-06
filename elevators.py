import random

def choose_one(floors):
    return random.randrange(floors)

def choose_all(people, floors):
    return [choose_one(floors) for p in range(people)]

def num_chosen(choices):
    return len(set(choices))

def main(n=1000):
    people = range(1, 9)
    floors = range(1, 9)
    result = {}
    for p in people:
        for f in floors:
            total = 0
            for i in range(n):
                total += num_chosen(choose_all(p, f))
            avg = total / float(n)
            result[(p, f)] = avg
    for key in sorted(result):
        print(key, result[key])

main()

"""

(n, m):  p(1)         p(2)  E
(2, 2):  1/2          1/2   3/2
(2, 3):  1/3          2/3   5/3
(2, 4):  1/4          3/4   7/4
(2, 5):  1/5          4/5   9/5
pattern: (1/m)^(n-1)
                                     (m^n - m - n!) / m^n
(n, m):  p(1)  p(2)   p(3)   E       (m / m^n) + min(m, n) * min(m,n)! / m^n 
(3, 2):  1/4   3/4           7/4     
(3, 3):  1/9   6/9    2/9    19/9    n! / k!(n - k)! * (k^n - k) / m^n  P(n, m, k) = C(m, k) * (k^n - C(k, i) * ()
(3, 4):  4/64  36/64  24/64  148/64  9/4

"""
