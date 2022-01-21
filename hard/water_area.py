def waterArea(heights):
    if not heights:
        return 0
    max_height = heights[0]
    max_index = 0
    for index in range(1, len(heights)):
        if heights[index] > max_height:
            max_height = heights[index]
            max_index = index
    if not max_height:
        return 0
    water = 0
    previous_max = 0
    for index in range(max_index):
        if heights[index] < previous_max:
            water += previous_max - heights[index]
        if heights[index] > previous_max:
            previous_max = heights[index]
    previous_max = 0
    for index in range(len(heights) - 1, max_index, -1):
        if heights[index] < previous_max:
            water += previous_max - heights[index]
        if heights[index] > previous_max:
            previous_max = heights[index]
    return water
