from heapq import heappush, heappop


def sortKSortedArray(array, k):
    heap = []
    heap_size = k + 1
    for index in range(min(heap_size, len(array))):
        heappush(heap, array[index])
    for index in range(len(array)):
        if heap:
            array[index] = heappop(heap)
        if index + heap_size < len(array):
            heappush(heap, array[index + heap_size])
    return array
