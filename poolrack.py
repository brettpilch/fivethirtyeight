"""
You own a start-up, RoboRackers™, that makes robots that can rack pool balls.
To operate the robot, you give it a template, such as the one shown below.
(The template only recognizes the differences among stripes, solids and the eight ball.
None of the other numbers matters.)

Template, where 0 means "solid", 1 means "stripe", and 8 means "8-ball":

           0
          1 0
         0 8 1
        1 0 1 0
       0 1 1 0 1

This will be represented in code as a tuple:

template = (0, 1, 0, 0, 8, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1)

First, the robot randomly corrals all of the balls into the wooden triangle.
From there, the robot can either swap the location of two balls or rotate the entire
rack 120 degrees in either direction. The robot continues performing these operations
until the balls’ formation matches the template, and it always uses the fewest number
of operations possible to do so.

Using the template given above — a correct rack for a standard game of eight-ball —
what is the maximum number of operations the robot would perform? What starting position
would yield this? How about the average number of operations?

Extra credit: What is the maximum number of operations the robot would perform using any
template? Which template and starting position would yield this?
"""

from collections import deque, defaultdict
from numpy import mean
from itertools import combinations
import random

template = (0, 1, 0, 0, 8, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1)
right_idx = (10, 11, 6, 12, 7, 3, 13, 8, 4, 1, 14, 9, 5, 2, 0)
left_idx = (14, 9, 13, 5, 8, 12, 2, 4, 7, 11, 0, 1, 3, 6, 10)

def rotate_right(rack):
    """return the rack obtained by rotating 120 degrees clockwise"""
    return tuple([rack[i] for i in right_idx])

def rotate_left(rack):
    """return the rack obtained by rotating 120 degrees counter-clockwise"""
    return tuple([rack[i] for i in left_idx])

def swap(rack, i, j):
    """return the rack obtained by swapping the balls at indices i and j"""
    new_rack = list(rack)
    new_rack[i], new_rack[j] = rack[j], rack[i]
    return tuple(new_rack)

def find_all_racks(template):
    """return a dict mapping every possible rack to the number of moves
    it takes to get from that rack to the template"""
    moves_to_rack = {template: 0}
    frontier = deque([(template, 0)])
    indices = list(range(len(template)))
    index_pairs = list(combinations(indices, 2))
    while frontier:
        this_rack, moves = frontier.popleft()
        moves += 1
        next_racks = set([rotate_right(this_rack), rotate_left(this_rack)])
        for i, j in index_pairs:
            next_racks.add(swap(this_rack, i, j))
        for rack in next_racks:
            if rack not in moves_to_rack:
                moves_to_rack[rack] = moves
                frontier.append((rack, moves))
    return moves_to_rack

def main():
    """print out all relevant statistics"""
    moves_to_rack = find_all_racks(template)
    max_moves = max(moves_to_rack.values())
    mean_moves = mean(list(moves_to_rack.values()))
    racks_from_moves = defaultdict(list)
    for rack, move in moves_to_rack.items():
        racks_from_moves[move].append(rack)

    print("max moves: {}".format(max_moves))
    print("one of the worst racks: {}".format(random.choice(racks_from_moves[6])))
    print("mean moves: {}".format(mean_moves))

    for moves in sorted(racks_from_moves.keys()):
        num_racks = len(racks_from_moves[moves])
        print("{} moves: {}".format(moves, num_racks))

if __name__ == "__main__":
    main()
