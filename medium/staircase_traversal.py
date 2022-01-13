def getMaxArray(maximum):
    max_array = [1 for i in range(maximum)]
    prev_sum = 2
    for i in range(2, maximum):
        max_array[i] = prev_sum
        prev_sum += max_array[i]
    return max_array
        
def updateMaxArray(max_array):
    new_element = sum(max_array)
    max_array.pop(0)
    max_array.append(new_element)
    
def staircaseTraversal(height, maxSteps):
    max_array = getMaxArray(maxSteps)
    for n in range(maxSteps, height + 1):
        updateMaxArray(max_array)       
    return max_array[-1]