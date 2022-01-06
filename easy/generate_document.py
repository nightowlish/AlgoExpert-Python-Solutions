def generateDocument(characters, document):
    char_map = {}
    for char in characters:
        try:
            char_map[char] += 1
        except:
            char_map[char] = 1
    for char in document:
        if not char in char_map or not char_map[char]:
            return False
        char_map[char] -= 1
    return True
        
