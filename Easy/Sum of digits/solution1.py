# # to find the number of digits in a number
# # import math
# # digits = int(math.log10(n))+1

# def SUM(n):
#     if n == 0:
#         return 0
#     digit = n % 10
#     return  digit + SUM(n//10)
# print(SUM(1432))

# def prod(n):
#     if n%10 == n:
#         return n
#     digit = n % 10
#     return  digit * prod(n//10)
# print(prod(1432))


# # BEST WAY TO REVERSE A NUMBER USING RECURSION:-
# def reverse(n, r):
#     if n==0:
#         return r
#     else:
#         return reverse(n//10, r*10 + n%10)

# def isPalindrome(n):
#     if n == reverse(n,0):
#         return True
#     return False

# print(isPalindrome(121))

def cntZeroes(n,cnt):
    if n == 0:
        return cnt
    
    if n % 10 == 0:
        cntZeroes(n//10, cnt + 1)
    else:
        cntZeroes(n//10, cnt)

print(cntZeroes(100, 0))
