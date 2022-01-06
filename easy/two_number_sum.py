def twoNumberSum(array, targetSum):
    mapping = {}
    for element in array:
        difference = targetSum - element
        if element in mapping:
            return [mapping[element], element]
        mapping[difference] = element
    return []
