class Coordinates:
    def __init__(self, x, y, max_x, max_y):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y

def visitBorder(matrix, coords):
    if matrix[coords.x][coords.y] != 1:
        return
    matrix[coords.x][coords.y] = 2
    if coords.x:
        coords.x -= 1
        visitBorder(matrix, coords)
        coords.x += 1
    if coords.y:
        coords.y -= 1
        visitBorder(matrix, coords)
        coords.y += 1
    if coords.x + 1 < coords.max_x:
        coords.x += 1
        visitBorder(matrix, coords)
        coords.x -= 1
    if coords.y + 1 < coords.max_y:
        coords.y += 1
        visitBorder(matrix, coords)
        coords.y -= 1

def getFormattedMatrix(matrix, max_x, max_y):
    for x in range(max_x):
        for y in range(max_y):
            if matrix[x][y] == 2:
                matrix[x][y] = 1
            elif matrix[x][y] == 1:
                matrix[x][y] = 0
    return matrix

def removeIslands(matrix):
    max_x = len(matrix)
    if not max_x:
        return matrix
    max_y = len(matrix[0])
    if not max_y:
        return matrix
    coords = Coordinates(0, 0, max_x, max_y)
    for y in range(max_y):
        coords.y = y
        visitBorder(matrix, coords)
    coords.y = max_y - 1
    for x in range(1, max_x - 1):
        coords.x = x
        visitBorder(matrix, coords)
    coords.x = max_x - 1
    for y in range(max_y - 1, -1, -1):
        coords.y = y
        visitBorder(matrix, coords)
    coords.y = 0
    for x in range(max_x - 2, 0, -1):
        coords.x = x
        visitBorder(matrix, coords)
    return getFormattedMatrix(matrix, max_x, max_y)
