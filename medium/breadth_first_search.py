from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
        
    def breadthFirstSearch(self, array):
        queue = deque()
        queue.append(self)
        while queue:
            child = queue.popleft()
            array.append(child.name)
            for subchild in child.children:
                queue.append(subchild)
        return array
        