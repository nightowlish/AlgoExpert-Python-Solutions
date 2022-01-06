def sortedSquaredArray(array):
    squares = []
    index_small = 0
    index_big = len(array) - 1
    while index_small != index_big:
        if abs(array[index_small]) > abs(array[index_big]):
            squares.insert(0, array[index_small]*array[index_small])
            index_small += 1
        else:
            squares.insert(0, array[index_big]*array[index_big])
            index_big -= 1
    squares.insert(0, array[index_small]*array[index_small])
    return squares
