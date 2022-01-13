class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        

def getLinkedListValue(linkedList):
    return linkedList.value if linkedList else 0

def getNextLink(linkedList):
    return linkedList.next if linkedList else linkedList
    
def getSum(nodeOne, nodeTwo, carry):
    return getLinkedListValue(nodeOne) + getLinkedListValue(nodeTwo) + carry
    
def sepparateCarry(digitSum):
    if digitSum >= 10:
        return digitSum - 10, 1
    return digitSum, 0

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    head = None
    current_node = None
    carry = 0
    while linkedListOne or linkedListTwo or carry:
        digit_sum = getSum(linkedListOne, linkedListTwo, carry)
        linkedListOne = getNextLink(linkedListOne)
        linkedListTwo = getNextLink(linkedListTwo)
        digit_sum, carry = sepparateCarry(digit_sum)
        new_node = LinkedList(digit_sum)
        if not head:
            head = new_node
            continue
        if not current_node:
            current_node = new_node
            head.next = current_node
            continue
        current_node.next = new_node
        current_node = current_node.next
    return head
