class Pair:
    def __init__(self, first_int, second_int):
        self.first_int = first_int
        self.second_int = second_int
        self.sum = self.first_int + self.second_int
        
    def is_duplicate_sum(self, pair):
        if self.second_int >= pair.first_int:
            return True
        return False
            

def getPairs(array):
    pairs = {}
    array_len = len(array)
    for first_index in range(array_len - 1):
        for second_index in range(first_index + 1, array_len):
            min_int = min(array[first_index], array[second_index])
            max_int = max(array[first_index], array[second_index])
            pair = Pair(min_int, max_int)
            try:
                pairs[pair.sum].append(pair)
            except:
                pairs[pair.sum] = [pair]
    return pairs
    
def fourNumberSum(array, target):
    results = []
    if len(array) < 4:
        return results
    pairs = getPairs(array)

    for first_sum, first_pairs in pairs.items():
        second_sum = target - first_sum
        if not second_sum in pairs:
            continue
        for first_pair in first_pairs:
            for second_pair in pairs[second_sum]:
                if first_pair.is_duplicate_sum(second_pair):
                    continue
                result = [first_pair.first_int, first_pair.second_int, second_pair.first_int, second_pair.second_int]
                results.append(result)
    return results
