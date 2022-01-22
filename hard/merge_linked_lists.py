class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeSortedLinkedLists(headOne, headTwo):
    head = headOne
    while headTwo:
        while headOne.next and headOne.next.value <= headTwo.value:
            headOne = headOne.next
        if not headOne.next:
            headOne.next = headTwo
            return headOne
        headOneNext = headOne.next
        headTwoNext = headTwo.next
        headOne.next = headTwo
        headTwo.next = headOneNext
        headTwo = headTwoNext
    return head

def mergeLinkedLists(headOne, headTwo):
    if not headOne:
        return headTwo
    if not headTwo:
        return headOne
    if headOne.value < headTwo.value:
        mergeSortedLinkedLists(headOne, headTwo)
        return headOne
    else:
        mergeSortedLinkedLists(headTwo, headOne)
        return headTwo
