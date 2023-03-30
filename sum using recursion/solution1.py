arr = [1,2,3,4,5,6,7,8,9,10]
size = len(arr)


def sol(arr,size):
    if size == 0:
        return 0
    return arr[len(arr)-size] + sol(arr, size-1)

print(sol(arr, size))