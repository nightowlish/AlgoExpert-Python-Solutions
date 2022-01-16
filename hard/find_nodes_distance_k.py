from collections import deque


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class NodeInfo:
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


def getParents(node, parent=None):
    parents = {}
    parents = {node.value: parent}
    if node.left:
        left_parents = getParents(node.left, parent=node)
        parents.update(left_parents)
    if node.right:
        right_parents = getParents(node.right, parent=node)
        parents.update(right_parents)
    return parents
    
def getTargetNode(node, target):
    if not node:
        return None
    if node.value == target:
        return node
    target_node = getTargetNode(node.left, target)
    if target_node:
        return target_node
    target_node = getTargetNode(node.right, target)
    if target_node:
        return target_node
    return None

def findNodesDistanceK(tree, target, k):
    nodes = []
    if not tree:
        return nodes
    parents = getParents(tree)
    target_node = getTargetNode(tree, target)
    if not target_node:
        return nodes        
    visited = {target}
    node_info = NodeInfo(target_node, 0)
    queue = deque()
    # start from target node
    queue.append(node_info) 
    while queue:
        node_info = queue.popleft()
        if node_info.distance == k:
            # took one too many nodes, must put it back
            queue.append(node_info)
            # stop appending nodes since all of the rest are too far from the target
            break
        if parents[node_info.node.value] and not parents[node_info.node.value].value in visited:
            # append the parent node
            new_node = NodeInfo(parents[node_info.node.value], node_info.distance + 1)
            queue.append(new_node)
            visited.add(new_node.node.value)
        if node_info.node.left and not node_info.node.left.value in visited:
            # append the left child
            new_node = NodeInfo(node_info.node.left, node_info.distance + 1)
            queue.append(new_node)
            visited.add(new_node.node.value)
        if node_info.node.right and not node_info.node.right.value in visited:
            # append the right child
            new_node = NodeInfo(node_info.node.right, node_info.distance + 1)
            queue.append(new_node)
            visited.add(new_node.node.value)
    # all nodes in queue are exactly at k distance from target
    while queue:
        node_info = queue.popleft()
        nodes.append(node_info.node.value)
    return nodes
