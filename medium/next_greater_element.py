def nextGreaterElement(array):
    result = [-1 for element in array]
    stack = []
    for index in range(len(array)):
        while stack and array[stack[-1]] < array[index]:
            result[stack[-1]] = array[index]
            stack.pop()
        stack.append(index)
    for index in range(len(array)):
        while stack and array[stack[-1]] < array[index]:
            result[stack[-1]] = array[index]
            stack.pop()
    return result
