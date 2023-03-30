
def kthGrammar(n, k):

    if n == 1 and k == 1:
        return 0
    
    half = pow(2,n-2)

    if k > half:
        k -= half
        return 1 - kthGrammar(n-1, k)
    else:
        return kthGrammar(n-1, k)
#needs to be traced
print(kthGrammar(4,8))