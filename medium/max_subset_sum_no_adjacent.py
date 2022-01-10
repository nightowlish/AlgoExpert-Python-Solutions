def maxSubsetSumNoAdjacent(array):
    array_len = len(array)
    if array_len == 0:
        return 0
    if array_len == 1:
        return array[0]
    if array_len == 2:
        return max(array[0], array[1])
    sums_array = [array[0], max(array[0], array[1])]
    for index in range(2, array_len):
        next_sum = max(sums_array[1], sums_array[0] + array[index])
        sums_array[0] = sums_array[1]
        sums_array[1] = next_sum
    return sums_array[1]
