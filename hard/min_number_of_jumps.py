def minNumberOfJumps(array):
    if not array or len(array) == 1:
        return 0
    jumps = [None for element in array]
    jumps[0] = 0
    for index in range(1, len(array)):
        for jump_index in range(index):
            if jump_index + array[jump_index] < index:
                continue
            if jumps[index] is None:
                jumps[index] = jumps[jump_index] + 1
                continue
            jumps[index] = min(jumps[index], jumps[jump_index] + 1)
    return jumps[-1]
