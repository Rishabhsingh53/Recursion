def reverse(string,size):
    
    if size == 0:
        return
    
    return reverse(string + 1, size-1)
    ans += string[0]

print(reverse('hello', 5))
