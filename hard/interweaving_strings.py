def interweavingStrings(str1, str2, str_combined):
    if not str_combined:
        return True
    if not str1:
        return str2 == str_combined
    if not str2:
        return str1 == str_combined
    if str1[0] != str_combined[0] and str2[0] != str_combined[0]:
        return False
    first_char = str_combined[0]
    str_combined = str_combined[1:]
    if str1[0] == str2[0]:
        return interweavingStrings(str1[1:], str2, str_combined) or interweavingStrings(str1, str2[1:], str_combined)
    if str1[0] == first_char:
        str1 = str1[1:]
    elif str2[0] == first_char:
        str2 = str2[1:]
    return interweavingStrings(str1, str2, str_combined)
