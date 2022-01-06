class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        
def branchSums(node, prev=0):
    prev += node.value
    if node.left:
        left_values = branchSums(node.left, prev=prev)
        if node.right:
            right_values = branchSums(node.right, prev=prev)
            left_values.extend(right_values)
        return left_values
    elif node.right:
        right_values = branchSums(node.right, prev=prev)
        return right_values
    else:
        return [prev]
