def reverseWordsInString(string):
    reversed = [] 
    current_word = [] 
    whitespace_count = 0 
    in_word = False 
    for char in string[::-1]:
        if in_word:
            if char == ' ':
                in_word = False
                reversed.append(''.join(current_word[::-1]))
                current_word = []
                whitespace_count = 1
            else:
                current_word.append(char)
        else:
            if char == ' ':
                whitespace_count += 1
            else:
                reversed.append(' ' * whitespace_count)
                whitespace_count = 0
                in_word = True
                current_word.append(char)
    if in_word:
        reversed.append(''.join(current_word[::-1]))
    else:
        reversed.append(' ' * whitespace_count)
    return ''.join(reversed)
