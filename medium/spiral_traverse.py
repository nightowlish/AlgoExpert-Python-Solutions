def spiralTraverse(matrix):
    matrix_n = len(matrix)
    if not matrix_n:
        return []
    if matrix_n == 1:
        return matrix[0]
    matrix_m = len(matrix[0])
    if matrix_m == 1:
        array = []
        for line in matrix:
            array.extend(line)
        return array

    linear_array = matrix[0]
    for i in range(1, matrix_n - 1):
        linear_array.append(matrix[i][matrix_m - 1])
    linear_array.extend(matrix[-1][::-1])
    for i in range(matrix_n - 2, 0, -1):
        linear_array.append(matrix[i][0])

    matrix = [element for element in [row[1:-1] for row in matrix[1:-1]] if element]
    inner_array = spiralTraverse(matrix)
    linear_array.extend(inner_array)
    
    return linear_array