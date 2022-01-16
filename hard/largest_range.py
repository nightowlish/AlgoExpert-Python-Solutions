class RangeMap:
    def __init__(self):
        self.starts_at = {} # {start of range: length of range}
        self.ends_at = {} # {end of range: length of range}
        
    def insert_value(self, value):
        if value in self.starts_at or value in self.ends_at:
            # case: value was already processed
            return
        prev_value = value - 1
        next_value = value + 1
        if prev_value in self.ends_at and next_value in self.starts_at:
            # case: value ties together two existing ranges
            self.merge(value)
            return
        if prev_value in self.ends_at:
            # case: value extends the end of an existing range
            length = self.ends_at[prev_value]
            length += 1
            del self.ends_at[prev_value]
            self.ends_at[value] = length
            self.starts_at[value - length + 1] += 1
        elif next_value in self.starts_at:
            # case: value extends the start of an existing range
            length = self.starts_at[next_value]
            length += 1
            del self.starts_at[next_value]
            self.starts_at[value] = length
            self.ends_at[value + length - 1] += 1
        else:
            # case: value is not related to any existing range
            self.ends_at[value] = 1
            self.starts_at[value] = 1
            
    def merge(self, value):
        next_length = self.starts_at[value + 1]
        prev_length = self.ends_at[value - 1]
        current_length = next_length + prev_length + 1
        self.starts_at[value - self.ends_at[value - 1]] = current_length
        self.ends_at[value + self.starts_at[value + 1]] = current_length
        del self.starts_at[value + 1]
        del self.ends_at[value - 1]
            
    def get_largest_range(self):
        max_range_start = 0
        max_range_length = 0
        for range_start, range_length in self.starts_at.items():
            if range_length > max_range_length:
                max_range_length = range_length
                max_range_start = range_start
        return [max_range_start, max_range_start + max_range_length - 1]


def largestRange(array):
    range_map = RangeMap()
    for element in array:
        range_map.insert_value(element)
    return range_map.get_largest_range()
