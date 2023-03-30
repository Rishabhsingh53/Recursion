# def sumOfNaturalNumbers(x):

#     if ( x > 0 ):

#         return x + sumOfNaturalNumbers(x-1)
    
#     return 0

# print(sumOfNaturalNumbers(10))

# def sumOfDigits(n):
#     if n == 0:
#         return 0 

#     ans = n % 10 + sumOfDigits(n//10)
#     return ans 

# print(sumOfDigits(12345))

# def product(x,y):
    
#     if y == 1:
#         return x 
#     return x + product(x, y-1)

# print(product(100, 5))


def arraySortedOrNot(arr):
    # Calculating length
    n = len(arr)
    # Array has one or no element or the
    # rest are already checked and approved.
    if n == 1 or n == 0:
        return True
    # Recursion applied till last element
    return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])
arr = [20, 23, 23, 45, 78, 88]
print(arraySortedOrNot(arr))
