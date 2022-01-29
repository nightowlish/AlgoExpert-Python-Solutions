from heapq import heappush, heappop


class Heap:
    def __init__(self):
        self.heap = []
        
    @property
    def length(self):
        return len(self.heap)
        
    def add(self, number, max=False):
        number = self.get_number(number, max=max)
        heappush(self.heap, number)
        
    def peek(self, max=False):
        if not self.heap:
            return None
        return self.get_number(self.heap[0], max=max)
    
    def get_number(self, number, max=False):
        if max:
            number *= -1
        return number
    
    def pop(self, max=False):
        if not self.heap:
            return None
        return self.get_number(heappop(self.heap), max=max)


class MinHeap(Heap):
    def __init__(self):
        super().__init__()


class MaxHeap(Heap):
    def __init__(self):
        super().__init__()
    
    def add(self, number):
        super().add(number, max=True)
        
    def peek(self):
        return super().peek(max=True)
        
    def pop(self):
        return super().pop(max=True)


class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()       
        
    def insert(self, number):
        self.min_heap.add(number)
        self.rebalance_heaps()          
        self.median = self.calculate_median()       
        
    def rebalance_heaps(self):
        while self.max_heap.length < self.min_heap.length:
            self.max_heap.add(self.min_heap.pop())
        
    def calculate_median(self):
        if (self.min_heap.length + self.max_heap.length) % 2:
            return self.max_heap.peek()
        return (self.max_heap.peek() + self.min_heap.peek()) / 2

    def getMedian(self):
        return self.median
