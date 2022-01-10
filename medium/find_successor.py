class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        

def findSuccessor(tree, node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node 
    while node.parent:
        if node.parent.left:
            if node.parent.left.value == node.value:
                return node.parent
        node = node.parent
    return None
