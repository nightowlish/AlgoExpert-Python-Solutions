def classPhotos(redShirtHeights, blueShirtHeights):
    max_red = max(redShirtHeights)
    max_blue = max(blueShirtHeights)
    if max_red > max_blue:
        blueShirtHeights, redShirtHeights = redShirtHeights, blueShirtHeights
    elif max_red == max_blue:
        return False
    redShirtHeights.sort()
    blueShirtHeights.sort()
    for index in range(len(redShirtHeights)):
        if blueShirtHeights[index] <= redShirtHeights[index]:
            return False
    return True
    
