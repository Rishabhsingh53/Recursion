def minAndMax(arr,maxSoFar,minSoFar,n):

    if n == 0:
        return [maxSoFar , minSoFar]
    
    if maxSoFar < arr[n]:
        maxSoFar = arr[n]
    elif minSoFar > arr[n]:
        minSoFar = arr[n]
    
    return minAndMax(arr, maxSoFar, minSoFar, n - 1)
    
arr = [1, 4, 3, -5, -4, 8, 6]
ans = minAndMax(arr,arr[0],arr[0],len(arr) - 1)
print("Max so far:\t", ans[0])
print("Min so far:\t", ans[1])
