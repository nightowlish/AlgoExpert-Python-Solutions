def firstNonRepeatingCharacter(string):
    char_order = []
    char_map = {}
    for index, char in enumerate(string):
        try:
            char_map[char] += 1
        except:
            char_map[char] = 1
            char_order.append((char, index))
    for char, index in char_order:
        if char_map[char] == 1:
            return index
    return -1
    
