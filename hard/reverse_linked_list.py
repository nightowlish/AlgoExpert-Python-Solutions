class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    prev_node = None
    current_node = head
    next_node = current_node.next
    while current_node.next:
        current_node.next = prev_node
        prev_node = current_node        
        current_node = next_node
        next_node = next_node.next
    current_node.next = prev_node
    return current_node
