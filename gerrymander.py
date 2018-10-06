from itertools import product, combinations
from random import choice
from scipy.misc import comb

def neighbors(a, b):
    if a[0][0] == b[0][0]:
        if abs(a[0][1] - b[0][1]) == 1:
            return True
    if a[0][1] == b[0][1]:
        if abs(a[0][0] - b[0][0]) == 1:
            return True
    return False

def all_neighbors(cells):
    len_cells = len(cells)
    cells = set(cells)
    if len(cells) < len_cells:
        return False
    neighbor_set = {cells.pop()}
    found = True
    while found:
        found = False
        for neighbor in neighbor_set:
            for cell in cells:
                if neighbors(neighbor, cell):
                    neighbor_set.add(cell)
                    cells.remove(cell)
                    found = True
                    break
            else: continue
            break
    return len(neighbor_set) == len_cells

def valid_group(cells):
    blues = sum(1 for cell in cells if cell[1] == 0)
    return blues in [3, 0]

def separate_groups(groups):
    cells = set()
    for group in groups:
        for cell in group:
            if cell in cells:
                return False
            cells.add(cell)
    return True

def get_results(possible_results):
    iters = 0
    for result in possible_results:
        if iters % 1000000 == 0:
            print(iters, end = '\r')
        iters += 1
        if separate_groups(result):
            yield result

cells = product(range(5), range(5))
colors = [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0]
grid = zip(cells, colors)
possible_groups = combinations(grid, 5)
print(1)
groups = (group for group in possible_groups if all_neighbors(group) and valid_group(group))
print(2)
possible_results = combinations(groups, 5)
print(3)
results = get_results(possible_results)
# results = (result for result in possible_results if separate_groups(result))
print(4)
for result in results:
    print()
    for group in result:
        print(group)