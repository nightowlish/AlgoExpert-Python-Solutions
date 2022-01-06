def nodeDepths(node, current_depth=0):
    next_depth = current_depth + 1
    left_depths = 0
    right_depths = 0
    if node.left:
        left_depths = nodeDepths(node.left, current_depth=next_depth)
    if node.right:
        right_depths = nodeDepths(node.right, current_depth=next_depth) 
    return current_depth + left_depths + right_depths    


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
