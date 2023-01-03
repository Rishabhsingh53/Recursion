def sumOfNaturalNumbers(x):

    if ( x > 0 ):

        return x + sumOfNaturalNumbers(x-1)
    
    return 0

print(sumOfNaturalNumbers(10))