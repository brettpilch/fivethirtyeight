# which 4 coin denominations require the minimum number of coins:

def which_coins(amount, coin_list):
    """determine which coins are used to make a given amount"""
    tendered = []
    while amount:
        for coin in coin_list:
            if coin <= amount:
                tendered.append(coin)
                amount -= coin
                break
    return tendered

def compare_to_best(coin_list, best=((25, 10, 5, 1), 999999999)):
    """compare the current set of coins to the best set found so far
    and return the better set"""
    count = 0
    for amount in range(1, 100):
        tendered = which_coins(amount, coin_list)
        count += len(tendered)
        if count >= best[1]:
            return best
    else:
        return coin_list, count

def get_best_coins():
    """find the best set of 4 coins out of all possible combinations"""
    best = ((None, None, None, None), 9999999999999999)
    c0 = 1 # smallest coin must be a penny to tender $0.01
    for c1 in range(2, 98):
        for c2 in range(c1 + 1, 99):
            for c3 in range(c2 + 1, 100):
                this_coins = (c3, c2, c1, c0)
                best = compare_to_best(this_coins, best)
    return best

print(get_best_coins()) # --> (37, 11, 3, 1) 

# def test_which_coins():
#     assert which_coins(99, [25, 10, 5, 1]) == [25, 25, 25, 10, 10, 1, 1, 1, 1]
#     assert which_coins(1, [25, 10, 5, 1]) == [1]
#     assert which_coins(50, [25, 10, 5, 1]) == [25, 25]
#     assert which_coins(40, [25, 10, 5, 1]) == [25, 10, 5]
#     print('passed all tests')

# test_which_coins()