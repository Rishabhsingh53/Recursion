# Checking if the array is sorted or not using recursion 

# Intuition behind this is that we know for array to be sorted every two elements of the array must be sorted
def check(arr,i,j):
    
    # if we have reached at the end then return True
    if j > len(arr) - 1 :
        return True
    # if at any point we find that array is not sorted return False
    if arr[i] > arr[j]:
        return False
    # if the two elements are sorted then call the function again with next two elements
    return check(arr, j, j+1)


print(check([1,2,3,4,5,6,5], 0, 1))