def quick_select(array, k, start_index, end_index):
    pivot_index = start_index
    left_index = start_index + 1
    right_index = end_index
    while left_index <= right_index:
        if array[left_index] > array[pivot_index] and array[right_index] < array[pivot_index]:
            array[left_index], array[right_index] = array[right_index], array[left_index]
        if array[left_index] <= array[pivot_index]:
            left_index += 1
            continue
        if array[left_index] >= array[pivot_index]:
            right_index -= 1
            continue
    array[pivot_index], array[right_index] = array[right_index], array[pivot_index]
    if right_index == k:
        return array[right_index]
    if k < right_index:
        return quick_select(array, k, start_index, right_index - 1)
    else:
        return quick_select(array, k, right_index + 1, end_index)
            
def quickselect(array, k):
    return quick_select(array, k - 1, 0, len(array) -1)

