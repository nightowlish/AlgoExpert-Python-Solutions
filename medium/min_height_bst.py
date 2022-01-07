def minHeightBst(array):
    if not array:
        return None
    middle = len(array) // 2
    root = BST(array[middle])
    root.left = minHeightBst(array[:middle])
    root.right = minHeightBst(array[middle+1:])
    return root

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
