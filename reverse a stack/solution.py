def reverseStack(stack):
    
    if len(stack) == 0:
        return 

    ele = stack.pop()
    reverseStack(stack)
    insert(stack,ele)
    return stack

def insert(stack,ele):

    if len(stack) == 0:
        stack.append(ele)
        return 

    val = stack.pop()
    insert(stack, ele)
    stack.append(val)

print(reverseStack([1,2,3,4,5]))

# done by rishabh Singh 😎😎😁