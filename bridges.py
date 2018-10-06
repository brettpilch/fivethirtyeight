# 00... = 8
# 10000
# 10001
# 10100
# 01000
# 01010
# 01100
# 11100
# 11000

# (n + 1)^2 + n^2 = 2n^2 + 2n + 1
# 2^(2n^2 + n)
# 2^(2n^2 + n) - 2^(2n^2 - 1)

# 000..........
# ..........000

# p(no) = 16 / 32 = 0.5
# p(yes) = 0.5

# |||--|||--|||
# 000.......... = 2^10
# 1000.0....... = 2^8
# 1000.1..0.0.. = 2^6
# 1000.1..1000. = 2^4
# 1000.1..11000 = 2^3
# 100100
# 100xx001
# 0

# p(3, 2, 3, 2, 3) =
# 111.. = 4
# 101xx = 3
# 110.1 = 2
# 0111. = 2
# 10011 = 1
# 01011 = 1
# 00111 = 1
# = 14 * p(3, 2, 3)
# +
# 110.0 = 2
# 10010 = 1
# 01010 = 1
# = 4 * p(2., 2, 3)
# +
# 0110. = 2
# 00101 = 1
# 01001 = 1
# = 4 * p(.2, 2, 3)
# +
# 10100 = 1
# = 1 * p(1.1, 2, 3)
# +
# 1000. = 2

# 1vert >= 1
# 1islewith2bridges == 1vert
# 2vert == 1islewith2bridges
# 2islewith2bridges == 2vert
# 3vert == 2islewith2bridges

# 1vert == 2vert or 1vert == 1isle1 and 1isle1 == 1isle2 and 1isle2 == 2vert or ... and
# 1vert == 2vert == 3vert or 1vert

graphs = [{'a': ['b', 'c', 0, 0, 0],
           'b': ['a', 0, 'c', 'd', 0],
           'c': [0, 'a', 'b', 0, 'd'],
           'd': [0, 0, 0, 'b', 'c']},
          {'a': ['b', 'c', 'd', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'b': ['a', 0, 0, 'c', 0, 'e', 0, 0, 0, 0, 0, 0, 0],
           'c': [0, 'a', 0, 'b', 'd', 0, 'f', 0, 0, 0, 0, 0, 0],
           'd': [0, 0, 'a', 0, 'c', 0, 0, 'g', 0, 0, 0, 0, 0],
           'e': [0, 0, 0, 0, 0, 'b', 0, 0, 'f', 0, 'h', 0, 0],
           'f': [0, 0, 0, 0, 0, 0, 'c', 0, 'e', 'g', 0, 'h', 0],
           'g': [0, 0, 0, 0, 0, 0, 0, 'd', 0, 'f', 0, 0, 'h'],
           'h': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'e', 'f', 'g']},
          {'a': ['b', 'c', 'd', 'e', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'b': ['a', 0, 0, 0, 'c', 0, 0, 'f', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'c': [0, 'a', 0, 0, 'b', 'd', 0, 0, 'g', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'd': [0, 0, 'a', 0, 0, 'c', 'e', 0, 0, 'h', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'e': [0, 0, 0, 'a', 0, 0, 'd', 0, 0, 0, 'i', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'f': [0, 0, 0, 0, 0, 0, 0, 'b', 0, 0, 0, 'g', 0, 0, 'j', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'g': [0, 0, 0, 0, 0, 0, 0, 0, 'c', 0, 0, 'f', 'h', 0, 0, 'k', 0, 0, 0, 0, 0, 0, 0, 0, 0],
           'h': [0, 0, 0, 0, 0, 0, 0, 0, 0, 'd', 0, 0, 'g', 'i', 0, 0, 'l', 0, 0, 0, 0, 0, 0, 0, 0],
           'i': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'e', 0, 0, 'h', 0, 0, 0, 'm', 0, 0, 0, 0, 0, 0, 0],
           'j': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'f', 0, 0, 0, 'k', 0, 0, 'n', 0, 0, 0],
           'k': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g', 0, 0, 'j', 'l', 0, 'n', 0, 0, 0],
           'l': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'h', 0, 0, 'k', 'm', 0, 0, 'n', 0],
           'm': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'i', 0, 0, 'l', 0, 0, 0, 'n'],
           'n': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'j', 'k', 'l', 'm']}]

def is_connected(number, graph, target, n):
    for i in range(n, len(number), 2 * n + 1):
        if number[i - n: i + 1] == '0' * (n + 1):
            return False
    explored = set([0])
    frontier = ['a']
    while frontier:
        isle = frontier.pop()
        if isle not in explored:
            explored.add(isle)
            conns = graph[isle]
            adds = [conn for i, conn in enumerate(conns) if number[i] == '1' and conn not in explored]
            if target in adds:
                return True
            frontier.extend(adds)
    return False

def make_binary(number, length):
    output = ''
    new_number = number
    for i in range(length - 1, -1, -1):
        if new_number // (2**i):
            output += '1'
            new_number -= 2**i
        else:
            output += '0'
    return output

def test_all(n, verbose = False):
    total = 0
    bridges = 2 * (n**2) + 2 * n + 1
    isles = n**2 + n + 2
    for i in range(2**(bridges - n - 1), 2**bridges):
        if verbose and i % 100000 == 0:
            print('testing patterns {} - {} out of {}'.format(i, i + 99999, 2**bridges))
        number = make_binary(i, bridges)
        if is_connected(number, graphs[n - 1], chr(ord('a') + isles - 1), n):
            total += 1
    return total, 2**bridges, total / float(2**bridges)

print(test_all(2))