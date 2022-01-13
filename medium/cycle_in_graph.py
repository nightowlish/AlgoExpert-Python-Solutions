def hasCycle(edges, current_node, visited):
    if current_node in visited:
        return True
    visited.add(current_node)
    for next_node in edges[current_node]:
        if hasCycle(edges, next_node, set(visited)):
            return True
    return False

def cycleInGraph(edges):
    for starting_node, connected_nodes in enumerate(edges):
        if hasCycle(edges, starting_node, set()):
            return True
    return False
