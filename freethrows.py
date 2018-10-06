import random

def simulate_once():
    results = [1, 0]
    for shot in range(3, 100):
        probability = sum(results) / float(len(results))
        if random.random() < probability:
            results.append(1)
        else:
            results.append(0)
    return results

def simulate_multi(n):
    sims = []
    for i in range(n):
        results = simulate_once()
        if results[-1] == 1:
            probability = sum(results) / float(len(results))
            sims.append(probability)
    return sum(sims) / float(len(sims))

print simulate_multi(100000) # => approximately 0.667