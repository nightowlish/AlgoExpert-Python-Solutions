possibilities_map = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def getCombinations(digits):
    previous_combinations = ['']
    new_combinations = []
    for digit_options in digits:
        for exact_digit in digit_options:
            for previous_combination in previous_combinations:
                new_combinations.append(previous_combination + exact_digit)
        previous_combinations = new_combinations
        new_combinations = []
    return previous_combinations

def phoneNumberMnemonics(phoneNumber):
    possibilities = []
    for digit in phoneNumber:
        possibilities.append(possibilities_map[digit])
    return getCombinations(possibilities)
