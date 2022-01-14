def threeNumberSort(array, order):
    array_len = len(array)
    if array_len <= 1:
        return array
        
    index = 0
    first_middle = None
    end_pointer = array_len - 1
    while array[end_pointer] == order[2] and end_pointer:
        end_pointer -= 1
    
    while index < end_pointer:
        if array[index] == order[1]:
            if first_middle is None:
                first_middle = index
            index += 1
            continue
        if array[index] == order[2]:
            array[index], array[end_pointer] = array[end_pointer], array[index]
            while array[end_pointer] == order[2] and end_pointer:
                end_pointer -= 1
            continue
        if array[index] == order[0]:
            if first_middle != None:
                array[first_middle], array[index] = array[index], array[first_middle]
                first_middle += 1
            while array[index] == order[0] and index < array_len - 1:           
                index += 1
            continue
    if array[end_pointer] == order[0] and first_middle != None:
        array[end_pointer], array[first_middle] = array[first_middle], array[end_pointer]
    return array
