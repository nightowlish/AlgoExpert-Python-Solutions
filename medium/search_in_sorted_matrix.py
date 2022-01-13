def searchInSortedMatrix(matrix, target):
    max_x = len(matrix)
    if not max_x:
        return [-1, -1]
    max_y = len(matrix[0])
    if not max_y:
        return [-1, -1]
    good_min_x = 0
    good_max_x = max_x - 1
    good_min_y = 0
    good_max_y = max_y - 1
    while good_min_x < good_max_x or good_min_y < good_max_y:
        for x in range(good_min_x, good_max_x + 1):
            if matrix[x][good_min_y] > target:
                good_max_x -= 1
            if matrix[x][good_max_y] < target:
                good_min_x += 1
        for y in range(good_min_y, good_max_y + 1):
            if matrix[good_min_x][y] > target:
                good_max_y -= 1
            if matrix[good_max_x][y] < target:
                good_min_y += 1
    if matrix[good_min_x][good_min_y] == target:
        return good_min_x, good_min_y
    return -1, -1
