def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if not arrayOne:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False
        
    parent = arrayOne[0]
    leftOne = []
    rightOne = []
    leftTwo = []
    rightTwo = []
    for index in range(1, len(arrayOne)):
        if arrayOne[index] < parent:
            leftOne.append(arrayOne[index])
        else:
            rightOne.append(arrayOne[index])
        if arrayTwo[index] < parent:
            leftTwo.append(arrayTwo[index])
        else:
            rightTwo.append(arrayTwo[index])
    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)
    
