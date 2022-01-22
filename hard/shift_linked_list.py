class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    length = getLinkedListLength(head)
    k = -k % length
    if not k:
        return head
    new_head = getNewHead(head, k)
    concatenateLinkedLists(new_head, head)
    return new_head

def getLinkedListLength(head):
    length = 0
    current_node = head
    while current_node:
        length += 1
        current_node = current_node.next
    return length

def concatenateLinkedLists(head, tail):
    current_node = head
    while current_node.next:
        current_node = current_node.next
    current_node.next = tail

def getNewHead(head, k):
    current_node = head
    for _ in range(k - 1):
        current_node = current_node.next
    new_head = current_node.next        
    current_node.next = None
    return new_head
