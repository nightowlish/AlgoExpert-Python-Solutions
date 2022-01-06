def nonConstructibleChange(coins):
    coins.sort()
    max_possible_sum = 0
    for coin in coins:
        next_max = max_possible_sum + 1
        if coin > next_max:
            return next_max
        max_possible_sum += coin
    return max_possible_sum + 1
