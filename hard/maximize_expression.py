def maximizeExpression(array):
    if len(array) < 4:
        return 0
    a = [None for elem in array]
    a_b = [None for elem in array]
    a_b_c = [None for elem in array]
    a_b_c_d = [None for elem in array]
    
    a[0] = array[0]
    for index in range(1, len(array)):
        a[index] = max(a[index - 1], array[index])

    a_b[1] = a[0] - array[1]
    for index in range(2, len(array)):
        a_b[index] = max(a_b[index - 1], a[index - 1] - array[index])
        
    a_b_c[2] = a_b[1] + array[2]
    for index in range(3, len(array)):
        a_b_c[index] = max(a_b_c[index - 1], a_b[index - 1] + array[index])
        
    a_b_c_d[3] = a_b_c[2] - array[3]
    for index in range(4, len(array)):
        a_b_c_d[index] = max(a_b_c_d[index - 1], a_b_c[index - 1] - array[index])
        
    return a_b_c_d[-1]
