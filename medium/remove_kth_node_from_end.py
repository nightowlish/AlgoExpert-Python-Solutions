class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def getLinkedListLength(node):
    length = 1
    while node.next:
        node = node.next
        length += 1
    return length
    
def removeKthNodeFromEnd(head, k):
    linked_list_length = getLinkedListLength(head)
    if linked_list_length == k:
        head.value = head.next.value
        head.next = head.next.next
        return
    node = head
    for i in range(linked_list_length - k - 1):
        node = node.next
    while node:
        if node.next.next:
            node.next.value = node.next.next.value
        else:
            node.next = None
        node = node.next
