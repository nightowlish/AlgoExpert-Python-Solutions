def invertBinaryTree(tree):
    tree.left, tree.right = tree.right, tree.left
    if tree.left:
        invertBinaryTree(tree.left)
    if tree.right:
        invertBinaryTree(tree.right)
    return tree


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
