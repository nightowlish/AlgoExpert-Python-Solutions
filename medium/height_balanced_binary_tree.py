class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, height, balanced):
        self.height = height
        self.balanced = balanced


def getTreeInfo(tree):
    tree_info_left = getTreeInfo(tree.left) if tree.left else TreeInfo(0, True)
    tree_info_right = getTreeInfo(tree.right) if tree.right else TreeInfo(0, True)
    height_difference = abs(tree_info_left.height - tree_info_right.height)
    if tree_info_left.balanced and tree_info_right.balanced:
        balanced = True if height_difference <= 1 else False
    else:
        balanced = False
    height = max(tree_info_left.height, tree_info_right.height) + 1
    return TreeInfo(height, balanced)
    
def heightBalancedBinaryTree(tree):
    tree_info = getTreeInfo(tree)
    return tree_info.balanced
