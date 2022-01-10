def kadanesAlgorithm(array):
    max_sum = 0
    current_sum = 0
    for current_index in range(len(array)):
        current_sum += array[current_index]
        if current_sum < 0:
            current_sum = 0
        elif current_sum > max_sum:
            max_sum = current_sum
    return max_sum if max_sum > 0 else max(array)
