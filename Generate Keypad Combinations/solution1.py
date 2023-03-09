def printReverse(arr,idx):
    if len(arr) - 1 == idx:
        print(arr[idx])
        return
    
    printReverse(arr, idx + 1)

    print(arr[idx])
    
printReverse([1,2,3,4,5], 0)