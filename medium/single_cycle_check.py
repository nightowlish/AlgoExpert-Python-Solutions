def hasSingleCycle(array):
    visited_indexes = [False for element in array]
    array_len = len(array)
    index = 0
    original_index = 0
    while True:
        if visited_indexes[index]:
            if original_index == index:
                return all(visited_indexes)
            else:
                return False
        visited_indexes[index] = True
        index += array[index]
        index = index % array_len
