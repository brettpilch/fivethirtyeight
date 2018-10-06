import random

def baby_steps(n):
    loc = 0
    at_couch = 0
    for time in range(n):
        r = random.random()
        if r < 0.25: # move forward
            loc += 1
        elif r > 0.5: # move back
            loc -= 1
        if loc < 0: # can't go into the couch
            loc = 0
        if loc == 0: # increment any time the baby is at the couch
            at_couch += 1
    return at_couch / float(n)

print(baby_steps(1000000)) # --> a number close to 0.5