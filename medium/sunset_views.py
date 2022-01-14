def sunsetViews(buildings, direction):
    sunset_viewers = []
    tallest = 0
    if direction == 'WEST':
        generator = range(len(buildings)) 
    else:
        generator = range(len(buildings) - 1, -1, -1)
    for index in generator:
        if buildings[index] > tallest:
            sunset_viewers.append(index)
            tallest = buildings[index]
    if direction == 'WEST':
        return sunset_viewers
    return sunset_viewers[::-1]
