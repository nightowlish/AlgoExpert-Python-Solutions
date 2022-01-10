def getInitializedMatrix(n, m):
    matrix = [[0 for i in range(m + 1)] for i in range(n + 1)]
    matrix[0] = [i for i in range(m + 1)]
    for i in range(1, n + 1):
        matrix[i][0] = i
    return matrix

def levenshteinDistance(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    matrix = getInitializedMatrix(str1_len, str2_len)
    for i in range(1, str1_len + 1):
        for j in range(1, str2_len + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
    return matrix[-1][-1]
        
