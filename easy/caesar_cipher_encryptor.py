def caesarCipherEncryptor(string, key):
    max_ord = ord('z')
    len_ord = max_ord - ord('a') + 1
    key = key % len_ord
    new_string = []
    for i in range(0, len(string)):
        new_ord = ord(string[i]) + key
        if new_ord > max_ord:
            new_ord -= len_ord
        new_string.append(chr(new_ord))
    return ''.join(new_string)
