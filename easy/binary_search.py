def binarySearch(array, target):
    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2
        if target == array[middle_pointer]:
            return middle_pointer
        if target < array[middle_pointer]:
            right_pointer = middle_pointer - 1
        else:
            left_pointer = middle_pointer + 1
    return -1
