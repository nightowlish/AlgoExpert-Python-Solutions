def get_sign(a, b):
    if a < b:
        return -1
    if a == b:
        return 0
    if a > b:
        return 1

def isMonotonic(array):
    array_len = len(array)
    if array_len < 2:
        return True
    sign = 0
    for index in range(0, array_len - 1):
        new_sign = get_sign(array[index], array[index + 1])
        if new_sign == 0:
            continue
        if sign == 0:
            sign = new_sign
            continue
        if sign != new_sign:
            return False
    return True