def threeNumberSum(array, target_sum):
    array.sort()
    sums = []
    array_length = len(array)
    for middle_pointer in range(1, array_length - 1):
        left_pointer = 0
        right_pointer = array_length - 1
        while left_pointer < middle_pointer and middle_pointer < right_pointer:
            three_sum = array[left_pointer] + array[middle_pointer] + array[right_pointer]
            if three_sum < target_sum:
                left_pointer += 1
            elif three_sum > target_sum:
                right_pointer -= 1
            else:
                sums.append([array[left_pointer], array[middle_pointer], array[right_pointer]])
                left_pointer += 1
    sums.sort()
    return sums
