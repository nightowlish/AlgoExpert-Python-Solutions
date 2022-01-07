def merge_intervals(intervals, index_to_merge):
    intervals[index_to_merge - 1][1] = max(intervals[index_to_merge - 1][1], intervals[index_to_merge][1])
    intervals.pop(index_to_merge)

def mergeOverlappingIntervals(intervals):
    intervals.sort()
    intervals_len = len(intervals)
    index = 0
    while True:
        index += 1
        if index == intervals_len:
            break
        if intervals[index][0] >= intervals[index - 1][0] and intervals[index][0] <= intervals[index - 1][1]:
            merge_intervals(intervals, index)
            intervals_len -= 1
            index -= 1
    return intervals