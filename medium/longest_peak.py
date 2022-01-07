def get_peak(array):
    array_len = len(array)
    # if array is too short to be able to have a peak
    if array_len < 3:
        return 0, array_len
        
    peak = 0
    nr_parsed = 0
    up_peak_found = False
    down_peak_found = False
    for i in range(1, array_len):
        nr_parsed += 1
        if array[i-1] == array[i]:
            if up_peak_found and down_peak_found:
                # the end of the current peak
                return peak, nr_parsed
            else:
                # parsed integers are not a valid peak
                return 0, nr_parsed
        if array[i-1] > array[i]:
            if not up_peak_found:
                return 0, nr_parsed
            if not down_peak_found:
                down_peak_found = True
            peak += 1
        if array[i-1] < array[i]:
            if down_peak_found:
                # the current integer can be part of the start of the next peak
                nr_parsed -= 1
                return peak, nr_parsed
            if not up_peak_found:
                up_peak_found = True
                peak += 1
            peak += 1
    if not down_peak_found:
        # case where the received array is sorted
        return 0, nr_parsed
    # case where the whole received array is a peak
    return peak, nr_parsed
        
def longestPeak(array):
    if not array:
        return 0
    longest_peak = 0
    while array:
        peak, parsed_len = get_peak(array)
        array = array[parsed_len:]
        if peak > longest_peak:
            longest_peak = peak
    return longest_peak
        
