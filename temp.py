def moveZeros(nums): 
    zero = -1
    nonZero = -1

    for i in range(len(nums)):
        if nums[i] != 0:
            continue
        else:
            zero = i 
            for j in range(i,len(nums)):
                if nums[j] != 0:
                    nonZero = j
                    nums[zero],nums[nonZero] = nums[nonZero] ,nums[zero]
                    break
    
    return nums
            
print(moveZeros( [0,1,0,3,12]))