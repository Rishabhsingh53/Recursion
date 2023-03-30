def printSumTriangle(arr , n):
    if n == 0:
        return
    ans = [ ]
    for i  in range(n-1):
        ans.append(arr[i] + arr[i+1])
    printSumTriangle(ans, n-1)
    print(arr)

printSumTriangle([1,2,3,4,5],5)