class MapCoordinates:
    def __init__(self, x, y, max_x, max_y):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y


def getRiverSize(matrix, coord):
    matrix[coord.x][coord.y] = -1
    size = 1
    
    if coord.x:
        coord.x -= 1
        if matrix[coord.x][coord.y] == 1:
            size += getRiverSize(matrix, coord)
        coord.x += 1
    if coord.y:
        coord.y -= 1
        if matrix[coord.x][coord.y] == 1:
            size += getRiverSize(matrix, coord)
        coord.y += 1
    coord.x += 1
    if coord.x < coord.max_x:
        if matrix[coord.x][coord.y] == 1:
            size += getRiverSize(matrix, coord)
    coord.x -= 1
    coord.y += 1
    if coord.y < coord.max_y:
        if matrix[coord.x][coord.y] == 1:
            size += getRiverSize(matrix, coord)
    coord.y -= 1
    return size

def riverSizes(matrix):
    sizes = []
    max_x = len(matrix)
    if not max_x:
        return sizes
    max_y = len(matrix[0])
    if not max_y:
        return sizes
    coord = MapCoordinates(0, 0, max_x, max_y)
    for x in range(max_x):
        coord.set_x(x)
        for y in range(max_y):
            if matrix[x][y] != 1:
                continue
            coord.set_y(y)
            size = getRiverSize(matrix, coord)
            sizes.append(size)
    return sizes
            
