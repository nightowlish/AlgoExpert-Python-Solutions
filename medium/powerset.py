def powerset(array):
    powersets = [[]]
    for element in array:
        for index in range(len(powersets)):
            powersets.append(powersets[index] + [element])
    return powersets
