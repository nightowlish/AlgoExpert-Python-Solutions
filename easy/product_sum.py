def productSum(array, depth=1):
    total_sum = 0
    for element in array:
        if type(element) is int:
            total_sum += element * depth
        elif type(element) is list:
            total_sum += depth * productSum(element, depth=depth+1)
    return total_sum