def insertionSort(array):
    for i in range(1, len(array)):
        for si in range(0, i + 1):
            if array[i] >= array[si]:
                continue
            array[si], array[i] = array[i], array[si]
    return array
