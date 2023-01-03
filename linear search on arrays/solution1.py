def search(arr,target, i ):

    if i > len(arr) - 1:
        return -1 

    if target == arr[i]:
        return i 

    return search(arr, target , i + 1 )

print(search([1,2,4,5,8,5,22],8, 0))
    