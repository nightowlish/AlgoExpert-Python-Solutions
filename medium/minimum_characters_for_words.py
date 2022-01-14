def minimumCharactersForWords(words):
    chars_frequencies = {} 
    for word in words:
        remaining_chars = dict(chars_frequencies)
        for char in word:
            if not char in chars_frequencies:
                chars_frequencies[char] = 1
                remaining_chars[char] = 0
                continue
            if remaining_chars[char]:
                remaining_chars[char] -= 1
                continue
            chars_frequencies[char] += 1
    needed_chars = []
    for char, count in chars_frequencies.items():
        for i in range(count):
            needed_chars.append(char)
    return needed_chars
