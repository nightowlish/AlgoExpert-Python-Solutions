def isValidSubsequence(array, sequence):
    index_sequence = 0
    sequence_length = len(sequence)
    for element in array:
        if element == sequence[index_sequence]:
            index_sequence += 1
            if index_sequence == sequence_length:
                return True
    return False
