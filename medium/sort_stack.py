def insertInSortedStack(stack, value):
    if not stack:
        stack.append(value)
        return stack
    helper_stack = []
    while stack and stack[-1] > value:
        helper_stack.append(stack.pop())
    stack.append(value)
    while helper_stack:
        stack.append(helper_stack.pop())
    return stack

def sortStack(stack):
    if not stack:
        return stack
    value = stack.pop()
    if stack:
        stack = sortStack(stack)
    return insertInSortedStack(stack, value)
