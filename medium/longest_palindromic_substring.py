class Palindrome:
    def __init__(self, string):
        self.string = string
        self.length = len(self.string)


def getEvenPalindrome(string, index):
    length = 0
    try:
        while string[index - length] == string[index + length - 1]:
            length += 1
    except IndexError:
        pass # reached string bounds
    return Palindrome(string[index - length + 1:index + length - 1])

def getOddPalindrome(string, index):
    length = 0
    try:
        while string[index - length - 1] == string[index + length + 1]:
            length += 1
    except IndexError:
        pass # reached string bounds
    return Palindrome(string[index - length:index + length + 1])

def longestPalindromicSubstring(string):
    if not string:
        return string
    longest_palindrome = Palindrome(string[0])
    for index in range(1, len(string)):
        even = getEvenPalindrome(string, index)
        odd = getOddPalindrome(string, index)
        if even.length > odd.length:
            if even.length <= longest_palindrome.length:
                continue
            longest_palindrome.length = even.length
            longest_palindrome.string = even.string
        elif odd.length > even.length:
            if odd.length <= longest_palindrome.length:
                continue
            longest_palindrome.length = odd.length
            longest_palindrome.string = odd.string
    return longest_palindrome.string
