def subarraySort(array):
    # find the minimum and maximum elements that are out of order
    min_out_of_order = None
    max_out_of_order = None
    for index in range(1, len(array)):
        if array[index - 1] <= array[index]:
            continue
        if min_out_of_order is None:
            min_out_of_order = array[index]
        else:
            min_out_of_order = min(min_out_of_order, array[index])
        if max_out_of_order is None:
            max_out_of_order = array[index - 1]
        else:
            max_out_of_order = max(max_out_of_order, array[index - 1])
    # if no minimum was found (and consequently no maximum), the array is already sorted
    if min_out_of_order is None:
        return [-1, -1]
        
    # find the indexes of the subarray that needs sorting by counting:
    # the starting elements that are <= to the minimum out of order
    # the ending elements that are >= to the minimum out of order
    start_sorting_index = 0
    end_sorting_index = len(array) - 1
    for index in range(len(array)):
        if array[index] <= min_out_of_order:
            start_sorting_index += 1
        else:
            break
    for index in range(len(array) - 1, -1, -1):
        if array[index] >= max_out_of_order:
            end_sorting_index -= 1
        else:
            break
    return [start_sorting_index, end_sorting_index]
