# sorting an array using recursion 

def sort(arr):

    if (len(arr)) == 1:
        return 
    temp = arr[len(arr) -1 ]
    arr.pop()
    sort(arr)
    insert(arr,temp)
    return arr

def insert(arr,temp):

    if (len(arr) == 0 or arr[len(arr) -1 ] <= temp):
        arr.append(temp)
        return 

    ele = arr[ len(arr) -1 ]
    arr.pop()
    insert(arr, temp)
    arr.append(ele)
    return

print(sort([6,3,5,2,0,1]))