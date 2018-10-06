import scipy.stats
import math

def deciding_vote_prob(n):
    b = scipy.stats.binom(n, 0.5)
    return b.pmf(math.floor(n / 2))
    # n! / (2 * (n / 2)!) * 0.5**n

i = 2
while i < 1000:
    print(deciding_vote_prob(i))
    i *= 2

# print(deciding_vote_prob(1000000))