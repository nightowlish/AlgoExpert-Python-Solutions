from collections import deque


class MatrixInfo:
    def __init__(self, matrix, max_x, max_y):
        self.matrix = matrix
        self.max_x = max_x
        self.max_y = max_y


def containsNegatives(matrix_info):
    for x in range(matrix_info.max_x):
        for y in range(matrix_info.max_y):
            if matrix_info.matrix[x][y] < 0:
                return True
    return False

def processQueues(matrix_info, primary_queue, secondary_queue, passes=0):
    while primary_queue:
        x, y = primary_queue.popleft()
        if x and matrix_info.matrix[x - 1][y] < 0:
            matrix_info.matrix[x - 1][y] *= -1
            secondary_queue.append((x - 1, y))
        if y and matrix_info.matrix[x][y - 1] < 0:
            matrix_info.matrix[x][y - 1] *= -1
            secondary_queue.append((x, y - 1))
        if x + 1 < matrix_info.max_x and matrix_info.matrix[x + 1][y] < 0:
            matrix_info.matrix[x + 1][y] *= -1 
            secondary_queue.append((x + 1, y))
        if y + 1 < matrix_info.max_y and matrix_info.matrix[x][y + 1] < 0:
            matrix_info.matrix[x][y + 1] *= -1 
            secondary_queue.append((x, y + 1))
    if secondary_queue:
        return processQueues(matrix_info, secondary_queue, primary_queue, passes=passes + 1)
    return passes

def minimumPassesOfMatrix(matrix):
    primary_queue = deque()
    secondary_queue = deque()
    max_x = len(matrix)
    max_y = len(matrix[0])
    for x in range(max_x):
        for y in range(max_y):
            if matrix[x][y] > 0:
                primary_queue.append((x, y))
    matrix_info = MatrixInfo(matrix, max_x, max_y)
    passes = processQueues(matrix_info, primary_queue, secondary_queue)
    if containsNegatives(matrix_info):
        return -1
    return passes
