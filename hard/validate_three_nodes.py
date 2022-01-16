class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def isChildOf(nodeOne, nodeTwo):
    if not nodeTwo:
        return False
    if nodeOne.value < nodeTwo.value:
        return isChildOf(nodeOne, nodeTwo.left)
    if nodeOne.value > nodeTwo.value:
        return isChildOf(nodeOne, nodeTwo.right)
    if nodeOne.left == nodeTwo.left and nodeOne.right == nodeTwo.right:
        return True
    return isChildOf(nodeOne, nodeTwo.right)

def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isChildOf(nodeOne, nodeTwo.left) or isChildOf(nodeOne, nodeTwo.right):
        if isChildOf(nodeTwo, nodeThree.left) or isChildOf(nodeTwo, nodeThree.right):
            return True
        return False
    if isChildOf(nodeThree, nodeTwo.left) or isChildOf(nodeThree, nodeTwo.right):
        if isChildOf(nodeTwo, nodeOne.left) or isChildOf(nodeTwo, nodeOne.right):
            return True
        return False
    return False
