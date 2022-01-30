def quick_sort(array, start_index, end_index):
    if start_index >= end_index:
        return
    pivot_index = start_index
    left_index = start_index + 1
    right_index = end_index
    while right_index >= left_index:
        if array[left_index] <= array[pivot_index]:
            left_index += 1
            continue
        if array[right_index] >= array[pivot_index]:
            right_index -= 1
            continue
        if array[left_index] > array[pivot_index] or array[right_index] < array[pivot_index]:
            array[left_index], array[right_index] = array[right_index], array[left_index]
    array[pivot_index], array[right_index] = array[right_index], array[pivot_index]
    quick_sort(array, start_index, right_index - 1)
    quick_sort(array, right_index + 1, end_index)

def quickSort(array):
    if len(array) < 2:
        return array
    quick_sort(array, 0, len(array) - 1)
    return array
