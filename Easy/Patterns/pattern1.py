# # style 1 using same function
# def fun(r,c):

#     if r == 0:
#         return
    
#     if c < r:
#         print("*",end = " ")
#         fun(r, c + 1)
#     else:
#         print()
#         fun( r - 1, 0)    
# fun(4, 0)

# # Style 2 using two different functions
# def rows(n):
#     if n == 0:
#         return
    
#     print("*" , end=" ")
#     rows(n-1)


# def pattern(n,i):

#     if n == 0:
#         return

#     rows(i)
#     print()
#     pattern(n-1, i+1)

# pattern(5,1)

# style 3 using python power
def fun(n):

    if n == 0:
        return
    
    fun(n-1)
    print("*" * n )
    
fun(4)

def solution(arr):
    seen = {}

    for i in range(len(arr)):
        if arr[i] in seen:
            seen[arr[i]] += 1
        else:
            seen[arr[i]] = 1

    ans = 0
    val = 0
    for i in seen.keys():
        if seen[i] > val:
            ans = i
            val = seen[i]
    return ans

print(solution([1,1,2,2,3]))