def getInitializedMatrix(n, m):
    matrix = [[0 for i in range(n)] for i in range(m)]
    for i in range(n):
        matrix[0][i] = 1
    for i in range(m):
        matrix[i][0] = 1
    return matrix

def numberOfWaysToTraverseGraph(width, height):
    if width == 1 or height == 1:
        return 1
    matrix = getInitializedMatrix(width, height)
    for i in range(1, height):
        for j in range(1, width):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[-1][-1]
        
