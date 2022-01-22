def recursiveNumbersInString(string, numbers, cache):
    if string in cache:
        return cache[string]
    if string in numbers:
        return 1
    if len(string) == 1:
        return None
    min_spaces = None
    for index in range(1, len(string)):
        current_prefix = string[:index]
        remaining_string = string[index:]
        if not current_prefix in numbers:
            continue
        if not remaining_string in cache:
            remaining_spaces = recursiveNumbersInString(remaining_string, numbers, cache)
            cache[remaining_string] = remaining_spaces
        current_spaces = cache[remaining_string] + 1 if not cache[remaining_string] is None else None
        if current_spaces is None:
            continue
        min_spaces = current_spaces if min_spaces is None else min(min_spaces, current_spaces)
    return min_spaces   

def numbersInPi(pi, numbers):
    numbers = set(numbers)
    cache = {}
    nr_spaces = recursiveNumbersInString(pi, numbers, cache)
    return -1 if nr_spaces is None else nr_spaces - 1
