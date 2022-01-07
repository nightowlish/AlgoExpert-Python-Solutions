def inOrderTraverse(tree, array):
    if tree.left:
        inOrderTraverse(tree.left, array)
    array.append(tree.value)
    if tree.right:
        inOrderTraverse(tree.right, array)
    return array

def preOrderTraverse(tree, array):
    array.append(tree.value)
    if tree.left:
        preOrderTraverse(tree.left, array)
    if tree.right:
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    if tree.left:
        postOrderTraverse(tree.left, array)
    if tree.right:
        postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array
