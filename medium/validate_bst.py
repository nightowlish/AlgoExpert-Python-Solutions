class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_value=None, max_value=None):
    if not tree:
        return True
    if not max_value is None and tree.value >= max_value:
        return False
    if not min_value is None and tree.value < min_value:
        return False
    if tree.left and tree.left.value >= tree.value:
        return False
    if tree.right and tree.right.value < tree.value:
        return False
    if not validateBst(tree.left, min_value=min_value, max_value=tree.value):
        return False
    if not validateBst(tree.right, min_value=tree.value, max_value=max_value):
        return False
    return True
