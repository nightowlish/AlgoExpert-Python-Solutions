def selectionSort(array):
    for current_select_index in range(0, len(array)):
        current_minimum_index = current_select_index
        for i in range(current_select_index, len(array)):
            if array[current_minimum_index] > array[i]:
                current_minimum_index = i
        array[current_select_index], array[current_minimum_index] = array[current_minimum_index], array[current_select_index]
    return array    
