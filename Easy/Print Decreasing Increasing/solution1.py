
n = int(input())

ans = 0
if n != 0:
    ten = n // 10
    n = n - ten * 10
    ans += ten
if n != 0:
    five = n // 5
    n = n - five  *  5
    ans += five
if n != 0:
    two = n // 2
    n = n - two * 2 
    ans += two
one = 0
if n > 0:
    one = 1
    n -= 1
    ans += one
    
print(ans)