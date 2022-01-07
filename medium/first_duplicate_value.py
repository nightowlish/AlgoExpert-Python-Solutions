def firstDuplicateValue(array):
    for index in range(len(array)):
        current_value = array[index] if array[index] > 0 else array[index] * -1
        mapped_value = array[current_value - 1]
        if mapped_value < 0:
             return current_value
        array[current_value - 1] *= -1
    return -1
