def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    total_speed = 0
    for index in range(len(redShirtSpeeds)):
        total_speed += max(redShirtSpeeds[index], blueShirtSpeeds[index])
    return total_speed
