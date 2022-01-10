def numberOfWaysToMakeChange(n, denoms):
    ways_to_count = [0 for i in range(n + 1)]
    ways_to_count[0] = 1
    for denom in denoms:
        if denom > n:
            continue
        for i in range(denom, n + 1):
            ways_to_count[i] += ways_to_count[i - denom]
    return ways_to_count[n]
