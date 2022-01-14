class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        while string:
            current_dict = self.root
            for char in string:
                if not char in current_dict:
                    current_dict[char] = {}
                current_dict = current_dict[char]
            if not self.endSymbol in current_dict:
                current_dict[self.endSymbol] = True
            string = string[1:]
        
    def contains(self, string):
        current_dict = self.root
        for char in string:
            if not char in current_dict:
                return False
            current_dict = current_dict[char]
        if not self.endSymbol in current_dict:
            return False
        return current_dict[self.endSymbol]
