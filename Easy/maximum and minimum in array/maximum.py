def maximum(arr,idx):
    if idx == len(arr) - 1:
        return arr[idx]
    return max(arr[idx],maximum(arr,idx+1))
print(maximum([234,252,6,12,2532], 0))
