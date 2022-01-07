class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        return self

    def contains(self, value):
        if value > self.value:
            if self.right:
                return self.right.contains(value)
            return False
        if value < self.value:
            if self.left:
                return self.left.contains(value)
            return False
        return True

    def remove(self, value, parent=None):
        if value > self.value:
            self.right.remove(value, parent=self)
            return self
        if value < self.value:
            self.left.remove(value, parent=self)
            return self

        # cases where node to be removed is the current one     
        if not self.right and not self.left:
            # case: node is leaf
            if not parent:
                # case: node is the only node in the tree
                return self             
            if parent.value > self.value:
                parent.left = None
            else:
                parent.right = None
            return self
        if (self.left and not self.right) or (self.right and not self.left):
            # case: node has a single child
            if self.left:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            else:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
        else:
            # case: node has two children
            smallest_node = self.right.get_smallest_node()
            self.value = smallest_node.value
            self.right.remove(self.value, parent=self)
        return self
        
    def get_smallest_node(self):
        if self.left:
            return self.left.get_smallest_node()
        return self
