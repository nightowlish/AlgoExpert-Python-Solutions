class MinMaxInfo:
    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum

class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.info = []

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def pop(self):
        if not self.stack:
            return None
        self.info.pop()
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)
        if not self.info:
            minmax = MinMaxInfo(number, number)
        else:
            new_min = min(number, self.info[-1].min)
            new_max = max(number, self.info[-1].max)
            minmax = MinMaxInfo(new_min, new_max)
        self.info.append(minmax)

    def getMin(self):
        if not self.info:
            return None
        return self.info[-1].min
        
    def getMax(self):
        if not self.info:
            return None
        return self.info[-1].max
