class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if not self.tail:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if not self.head:
            self.head = nodeToInsert
            self.tail = nodeToInsert
            return
        if not node:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if nodeToInsert.prev:
            node.prev.next = nodeToInsert
        else:
            self.head = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if not self.head:
            self.head = nodeToInsert
            self.tail = nodeToInsert
            return
        if not node:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next:
            node.next.prev = nodeToInsert
        else:
            self.tail = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        current_position = 1
        current_node = self.head
        while current_node and current_position != position:
            current_node = current_node.next
            current_position += 1
        if current_node:
            self.insertBefore(current_node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        current_node = self.head
        while current_node:
            node_to_remove = current_node
            current_node = current_node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)
        
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNode(node)
        
    def removeNode(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    def containsNodeWithValue(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
