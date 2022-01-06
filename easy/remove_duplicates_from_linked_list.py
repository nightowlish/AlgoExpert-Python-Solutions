class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    head = linkedList
    node_to_append_to = linkedList
    last_value = linkedList.value 
    while linkedList.next:
        linkedList = linkedList.next 
        if linkedList.value != last_value:
            last_value = linkedList.value
            node_to_append_to = linkedList
            continue
        if not linkedList.next:
            node_to_append_to.next = None
            return head
        node_to_append_to.next = linkedList.next
    return head
