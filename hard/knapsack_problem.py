def getKnapsackIndexes(items, matrix):
    indexes = []
    x = len(matrix) - 1
    y = len(matrix[0]) - 1
    while x and y:
        if matrix[x][y] > matrix[x - 1][y]:
            # current item is used in the knapsack
            indexes.append(x - 1)
            y -= items[x - 1][1]
        x -= 1
    return indexes

def getKnapsackValue(items, matrix, x, y):
    if y < items[x - 1][1]:
        # cannot fit the current item's weight in the given capacity
        return matrix[x - 1][y]
    current_item_value = items[x - 1][0]
    current_item_weight = items[x - 1][1]
    value_with_current_item = matrix[x - 1][y - current_item_weight] + current_item_value
    value_without_current_item = matrix[x - 1][y]
    return max(value_with_current_item, value_without_current_item)

def getKnapsackMatrix(x, y):
    return [[0 for index in range(y + 1)] for index in range(x + 1)]

def knapsackProblem(items, capacity):
    matrix = getKnapsackMatrix(len(items), capacity)
    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[0])):
            matrix[x][y] = getKnapsackValue(items, matrix, x, y)
    knapsack = getKnapsackIndexes(items, matrix)
    return [matrix[-1][-1], knapsack]
