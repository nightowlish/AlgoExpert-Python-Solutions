def minNumberOfCoinsForChange(n, denoms):
    array = [None for i in range(n + 1)]
    array[0] = 0
    for denom in denoms:
        if denom > n:
            continue
        for index in range(denom, n + 1):
            if not array[index] is None:
                if not array[index - denom] is None:
                    array[index] = min(1 + array[index - denom], array[index])
                continue
            if not array[index - denom] is None:
                array[index] = 1 + array[index - denom]
    return array[n] if not array[n] is None else -1
