class MinHeap:
    def __init__(self, array):
        self.heap = None
        self.heap_length = None
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = array
        self.heap_length = len(self.heap)
        self.siftDown()
        return self.heap
        
    def siftDown(self):
        for index in range(self.heap_length // 2 + 1, -1, -1):
            self.siftDownIndex(index)

    def getValidIndex(self, index):
        if index < self.heap_length:
            return index
        return None

    def getLeftChildIndex(self, index):
        return self.getValidIndex(2 * index + 1)
        
    def getRightChildIndex(self, index):
        return self.getValidIndex(2 * index + 2)
        
    def switchIndex(self, parent_index, child_index):
        if self.heap[parent_index] <= self.heap[child_index]:
            return
        self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]

    def siftDownIndex(self, index):
        left_child_index = self.getLeftChildIndex(index)
        right_child_index = self.getRightChildIndex(index)
        
        if left_child_index is None:
            return
        if right_child_index is None:
            self.switchIndex(index, left_child_index)
            return
        min_child_index = left_child_index if self.heap[left_child_index] < self.heap[right_child_index] else right_child_index
        if self.heap[index] > self.heap[min_child_index]:
            self.switchIndex(index, min_child_index)
            self.siftDownIndex(min_child_index)
        
    def siftUp(self):
        for index in range(self.heap_length - 1, 0, -1):
            self.siftUpIndex(index)
        
    def siftUpIndex(self, index):
        if not index:
            return
        parent_index = (index - 1) // 2
        if self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.siftUpIndex(parent_index)
    
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def remove(self):
        if not self.heap:
            return
        self.heap_length -= 1
        if not self.heap_length:
            self.heap = []
            return
        removed_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftDownIndex(0)
        return removed_element

    def insert(self, value):
        if not self.heap:
            self.heap = [value]
            self.heap_length = 1
        else:
            self.heap.append(value)
            self.heap_length += 1
            self.siftUpIndex(self.heap_length - 1)
