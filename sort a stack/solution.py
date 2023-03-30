def sortStack(stack):
    
    if len(stack) == 1:
        return
    temp = stack.pop()
    sortStack(stack)
    insert(stack,temp)
    return stack

def insert(stack,temp):

    if len(stack) == 0 or stack[len(stack) - 1] <= temp:
        stack.append(temp)
        return
    ele = stack.pop()
    insert(stack, temp)
    stack.append(ele)
    
stack = []
stack.append(6)
stack.append(2)
stack.append(0)
stack.append(7)

print(sortStack(stack))