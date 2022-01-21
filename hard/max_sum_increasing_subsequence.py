def maxSumIncreasingSubsequence(array):
    if not array:
        return [0, []]
    partial_sums = [] # max sum possible until current index
    prev_indexes = [] # index of previous element of max sum at current index
    for index in range(len(array)):
        max_partial_sum = None
        max_prev_sum_index = None
        for prev_index in range(index - 1, -1, -1):
            if array[prev_index] >= array[index] or array[prev_index] <= 0:
                continue
            if max_partial_sum is None or partial_sums[prev_index] > max_partial_sum:
                max_partial_sum = partial_sums[prev_index]
                max_prev_sum_index = prev_index
        if max_partial_sum is None:
            partial_sums.append(array[index])
            prev_indexes.append(index)
        else:
            partial_sums.append(array[index] + max_partial_sum)
            prev_indexes.append(max_prev_sum_index)

    sum_total = partial_sums[0]
    sum_final_index = 0
    for index in range(1, len(partial_sums)):
        if partial_sums[index] > sum_total:
            sum_total = partial_sums[index]
            sum_final_index = index
    sum_components = [array[sum_final_index]]
    while sum_final_index != prev_indexes[sum_final_index]:
        sum_final_index = prev_indexes[sum_final_index]
        sum_components.append(array[sum_final_index])
    return [sum_total, sum_components[::-1]]
