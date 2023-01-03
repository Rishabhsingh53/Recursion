# Linear Search using Recursion 
def search(arr,target, i ):

    # if the index has crossed length of the array then return -1 i.e. not found
    if i > len(arr) - 1:
        return -1 
    # checking if target is equal to the ith element if yes return the index 
    if target == arr[i]:
        return i 
    # if not search from next index
    return search(arr, target , i + 1 )

ans = (search([1,2,4,5,8,5,22],8, 0))

if ans == -1:
    print("Target not found")
else:
    print("target found at index:\t", ans)