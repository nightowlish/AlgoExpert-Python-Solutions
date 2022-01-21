class MatrixSize:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getInitializedMatrix(x, y):
    matrix = []
    for row in range(x):
        matrix.append([])
        for line in range(y):
            matrix[row].append([])
    return matrix

def getPreviousLCS(matrix, x, y):
    if len(matrix[x - 1][y]) >= len(matrix[x][y - 1]):
        prev_lcs = matrix[x - 1][y]
    else:
        prev_lcs = matrix[x][y - 1]
    return prev_lcs 
        
def longestCommonSubsequence(str1, str2):
    if not str1 or not str2:
        return []
    matrix_size = MatrixSize(len(str1) + 1, len(str2) + 1)
    matrix = getInitializedMatrix(matrix_size.x, matrix_size.y)
    for x in range(1, matrix_size.x):
        for y in range(1, matrix_size.y):
            if str1[x - 1] == str2[y - 1]:
                matrix[x][y] = list(matrix[x - 1][y - 1])
                matrix[x][y].append(str1[x - 1])
            else:
                matrix[x][y] = getPreviousLCS(matrix, x, y)
    return matrix[-1][-1]
