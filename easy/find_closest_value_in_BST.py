def get_difference(value, target):
    return abs(target - value)

def findClosestValueInBst(tree, target):
    closest = tree.value
    closest_difference = get_difference(closest, target)
    while tree:
        current_difference = get_difference(tree.value, target)
        if current_difference <= closest_difference:
            closest = tree.value
            closest_difference = current_difference
        if target < tree.value:
            if tree.left:
                tree = tree.left
            else:
                return closest
        else:
            if tree.right:
                tree = tree.right
            else:
                return closest
            
    
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
