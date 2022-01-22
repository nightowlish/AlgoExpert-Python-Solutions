from collections import deque


class Node:
    def __init__(self, node, edges):
        self.node = node
        self.edges = edges


def dijkstrasAlgorithm(start, edges):
    distances = [None for _ in edges]
    distances[start] = 0
    visited = set()
    nodes_to_visit = deque([Node(start, edges[start])])
    while nodes_to_visit:
        current_node = nodes_to_visit.popleft()
        if current_node.node in visited:
            continue
        visited.add(current_node.node)
        for edge in current_node.edges:
            current_distance = distances[current_node.node] + edge[1]
            distances[edge[0]] = current_distance if distances[edge[0]] is None else min(current_distance, distances[edge[0]])
            destination_node = Node(edge[0], edges[edge[0]])
            nodes_to_visit.append(destination_node)
    result = []
    for index in range(len(edges)):
        distance = -1 if distances[index] is None else distances[index]
        result.append(distance)
    return result
        
