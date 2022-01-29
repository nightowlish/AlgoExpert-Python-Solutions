def indexEqualsValue(array):
    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer <= right_pointer:
        middle_pointer = left_pointer + (right_pointer - left_pointer) // 2
        middle_value = array[middle_pointer]
        if middle_value < middle_pointer:
            left_pointer = middle_pointer + 1
        elif middle_value == middle_pointer:
            if middle_pointer == 0:
                return middle_pointer
            elif array[middle_pointer - 1] < middle_pointer - 1:
                return middle_pointer
            else:
                right_pointer = middle_pointer - 1
        else:
            right_pointer = middle_pointer - 1
    return -1
