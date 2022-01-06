def bubbleSort(array):
    for outer_index in range(len(array)):
        for inner_index in range(outer_index + 1, len(array)):
            if array[outer_index] > array[inner_index]:
                array[outer_index], array[inner_index] = array[inner_index], array[outer_index]
    return array
