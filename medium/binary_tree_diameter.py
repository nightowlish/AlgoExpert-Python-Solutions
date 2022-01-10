class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def binaryTreeDiameterParse(tree):
    if not tree:
        return TreeInfo(0, 0)
    info_right = binaryTreeDiameterParse(tree.right)
    info_left = binaryTreeDiameterParse(tree.left)
    diameter = max(info_left.diameter, info_right.diameter, info_left.height + info_right.height)
    height = max(info_left.height, info_right.height) + 1
    return TreeInfo(diameter, height)
    
def binaryTreeDiameter(tree):
    return binaryTreeDiameterParse(tree).diameter

