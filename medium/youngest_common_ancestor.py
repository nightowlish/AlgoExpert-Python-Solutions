class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getNodeHeight(node):
    if not node.ancestor:
        return 0
    return 1 + getNodeHeight(node.ancestor)
    
def getNthAncestor(node, n):
    if n == 0:
        return node
    return getNthAncestor(node.ancestor, n - 1)
    
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    height_one = getNodeHeight(descendantOne)
    height_two = getNodeHeight(descendantTwo)
    if height_one > height_two:
        descendantOne = getNthAncestor(descendantOne, height_one - height_two)
    elif height_two > height_one:
        descendantTwo = getNthAncestor(descendantTwo, height_two - height_one)
    while True:
        if descendantOne.name == descendantTwo.name:
            return descendantOne
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor