def isPalindrome(string):
    string_length = len(string)
    for i in range(0, string_length // 2):
        if string[i] != string[string_length - 1 - i]:
            return False
    return True
