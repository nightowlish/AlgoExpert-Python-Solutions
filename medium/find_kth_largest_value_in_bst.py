class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k, array=None):
    array = [] if array is None else array
    if tree.right:
        res = findKthLargestValueInBst(tree.right, k, array)
        if not res is None:
            return res
    array.append(tree.value)
    if len(array) == k:
        return array[-1]
    if tree.left:
        res = findKthLargestValueInBst(tree.left, k, array)
        if not res is None:
            return res
