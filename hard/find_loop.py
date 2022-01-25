class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    first_pointer = head.next
    second_pointer = head.next.next
    while not first_pointer is second_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next.next
    first_pointer = head
    while not first_pointer is second_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    return first_pointer
