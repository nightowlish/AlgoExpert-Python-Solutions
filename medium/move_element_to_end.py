def moveElementToEnd(array, to_move):
    start_pointer = 0
    end_pointer = len(array) - 1
    while end_pointer > start_pointer:
        if array[end_pointer] == to_move:
            end_pointer -= 1
            continue
        while array[start_pointer] != to_move and start_pointer != end_pointer:
            start_pointer += 1
        if start_pointer == end_pointer:
            return array
        array[start_pointer], array[end_pointer] = array[end_pointer], array[start_pointer]
        start_pointer += 1
        end_pointer -= 1
    return array
