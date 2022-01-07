def get_absolute_difference(a, b):
    same_sign = a * b >= 0
    if same_sign:
        return abs(a - b)
    else:
        return abs(a) + abs(b)

def smallestDifference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    pointer_one = 0
    pointer_two = 0
    len_one = len(array_one)
    len_two = len(array_two)
    minimum_found = get_absolute_difference(array_one[0], array_two[0])
    minimum_values = [array_one[0], array_two[0]]
    while pointer_one < len_one and pointer_two < len_two:
        if not minimum_found:
            return minimum_values
        new_possible_minimum = get_absolute_difference(array_one[pointer_one], array_two[pointer_two])
        if new_possible_minimum < minimum_found:
            minimum_found = new_possible_minimum
            minimum_values = [array_one[pointer_one], array_two[pointer_two]]
        if array_one[pointer_one] < array_two[pointer_two]:
            pointer_one += 1
        else:
            pointer_two += 1
    return minimum_values