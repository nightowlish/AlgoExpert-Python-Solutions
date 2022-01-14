START_BRACKETS = {'(', '[', '{'}
BRACKETS_MAP = {')': '(', ']': '[', '}': '{'}

def balancedBrackets(string):
    open_brackets = []
    for char in string:
        if char in START_BRACKETS:
            open_brackets.append(char)
        elif char in BRACKETS_MAP:
            if not open_brackets:
                return False
            if open_brackets[-1] != BRACKETS_MAP[char]:
                return False
            else:
                open_brackets.pop()
    return not open_brackets
