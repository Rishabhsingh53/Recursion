def sumOfSquares(n):

    if n == 1:
        return 1
    else:
        return sumOfSquares(n-1) + n ** 2

print(sumOfSquares(5))
    