class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def update_traversal(matrix, point, traversal):
    traversal.append(matrix[point.y][point.x])

def getZigDown(matrix, point, traversal): 
    update_traversal(matrix, point, traversal)
    while point.x and point.y + 1 < len(matrix):
        point.x -= 1
        point.y += 1
        update_traversal(matrix, point, traversal)
    if point.y + 1 < len(matrix):
        point.y += 1
        return getZagUp(matrix, point, traversal)
    if point.x + 1 < len(matrix[0]):
        point.x += 1
        return getZagUp(matrix, point, traversal)
    return traversal

def getZagUp(matrix, point, traversal):
    update_traversal(matrix, point, traversal)
    while point.x + 1 < len(matrix[0]) and point.y:
        point.x += 1
        point.y -= 1
        update_traversal(matrix, point, traversal)
    if point.x + 1 < len(matrix[0]):
        point.x += 1
        return getZigDown(matrix, point, traversal)
    if point.y + 1 < len(matrix):
        point.y += 1
        return getZigDown(matrix, point, traversal)
    return traversal

def zigzagTraverse(array):
    if not array:
        return array
    if len(array) == 1:
        return array[0]
    if len(array[0]) == 1:
        return [row[0] for row in array]
    traversal = [array[0][0]]
    point = Point(0, 1)
    return getZagUp(array, point, traversal)
