def getPermutations(array, used=None):
    used = used if used else set()
    if len(array) - len(used) == 1:
        for element in array:
            if not element in used:
                return [[element]]

    permutations = []
    for element in array:
        if element in used:
            continue
        used.add(element)
        remaining_permutations = getPermutations(array, used=used)
        for remaining_permutation in remaining_permutations:
            remaining_permutation.append(element)
            permutations.append(remaining_permutation)
        used.remove(element)
    return permutations