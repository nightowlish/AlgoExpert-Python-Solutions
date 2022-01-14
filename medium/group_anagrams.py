def groupAnagrams(words):
    anagram_map = {}
    for index in range(len(words)):
        sorted_word = ''.join(sorted(words[index]))
        try:
            anagram_map[sorted_word].append(index)
        except:
            anagram_map[sorted_word] = [index]
    anagram_groups = []
    for anagram, indexes in anagram_map.items():
        anagram_groups.append([words[index] for index in indexes])
    return anagram_groups
