def findThreeLargestNumbers(array):
    largest = array[:3]
    largest.sort()
        
    for index in range (3, len(array)):
        if array[index] > largest[0]:
            if array[index] > largest[1]:
                largest[0] = largest[1]
                if array[index] > largest[2]:
                    largest[1] = largest[2]
                    largest[2] = array[index]
                else:
                    largest[1] = array[index]
            else:
                largest[0] = array[index]
    return largest
