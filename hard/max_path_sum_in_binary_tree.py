class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, largest_path, current_sum):
        self.largest_path = largest_path
        self.current_sum = current_sum


def get_info(node):
    if not node.left and not node.right:
        return TreeInfo(node.value, node.value)
    if not node.left or not node.right:
        node_with_children = node.left if node.left else node.right
        node_info = get_info(node_with_children)
        current_sum = node.value + node_info.current_sum
        return TreeInfo(node_info.largest_path, current_sum)
    left_info = get_info(node.left)
    right_info = get_info(node.right)
    current_sum = node.value + max(left_info.current_sum, right_info.current_sum)
    current_path = left_info.current_sum + node.value + right_info.current_sum
    largest_path = max(left_info.largest_path, current_path, right_info.largest_path, current_sum)
    return TreeInfo(largest_path, current_sum)

def maxPathSum(tree):
    if not tree:
        return 0
    tree_info = get_info(tree)
    return max(tree_info.largest_path, tree_info.current_sum)
