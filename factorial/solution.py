def factorial(x):

    if ( x > 0) :

        return x * factorial(x-1)

    return 1

print(factorial(4))