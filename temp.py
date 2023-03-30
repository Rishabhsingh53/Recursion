# # # # def moveZeros(nums): 
# # # #     zero = -1
# # # #     nonZero = -1
# # # #     for i in range(len(nums)):
# # # #         if nums[i] != 0:
# # # #             continue
# # # #         else:
# # # #             zero = i 
# # # #             for j in range(i,len(nums)):
# # # #                 if nums[j] != 0:
# # # #                     nonZero = j
# # # #                     nums[zero],nums[nonZero] = nums[nonZero] ,nums[zero]
# # # #                     break
# # # #     return nums            
# # # # print(moveZeros( [0,1,0,3,12] ))


# # # # intervals = [[1,100],[11,22],[1,11],[2,12]]
# # # # points = [[10,16],[1,6],[1,6],[1,6],[1,6],[1,6],[2,8],[1,6],[1,6],[7,12]]

# # # # def solution(points):
# # # #     intervals.sort(key = lambda x : x[0])
# # # #     res = [intervals[0]]
    
# # # #     for start , end in intervals[1:]:
# # # #         last = res[-1][1]
# # # #         if start < last and end < last:
# # # #             res.pop()
# # # #             res.append([start,end])
        
# # # #         elif start >= last:
# # # #             res.append([start,end])
# # # #         else:
# # # #             continue
# # # #     return len(intervals) - len(res)
# # # # print(solution(intervals))




# # # # def insertIntervals2(self, intervals, newInterval):
# # # #     intervals.append(newInterval)
# # # #     res = []
# # # #     for i in sorted(intervals, key=lambda x:x.start):
# # # #         if res and res[-1].end >= i.start:
# # # #             res[-1].end = max(res[-1].end, i.end)
# # # #         else:
# # # #             res.append(i)
# # # #     return res


"""
linked list technique:
This is the most common iterating technique in ll 
current and previous pointers
initialize curr with head and prev with none
while curr is not none 
    prev = curr
    curr = curr.next 
"""

"""

While Iterating through two strings of different length simultaneously

remeber to run two while loop after completion of first 
because one might end first and other is still left 

i.e. 
while i < len(a) and j < len(b):
    pass

while j < len(a):
    pass

while i < len(a):
    pass
"""

"""
Range Addition
suppose we are given a array of size n 
we want to perform q queries and each queries has 3 parameters: start end increment
return the final array after performing all queries
this can be done using prefix sum
what we will do is increment at the start index and decrement at (end + 1) index


"""

# # """
# # Majority Moore's Algorithm
# # """
# # # Greedy Gas Station
# # # def potd(cost,gas):
# # #     mn = min(cost)
# # #     idx = -1
# # #     tank = 0
# # #     diff = 0
# # #     for i in range(len(gas)):
# # #         if gas[i] >= cost[i] and gas[i] - cost[i] > diff:
# # #             diff = max(diff,gas[i] - cost[i])
# # #             idx = i
# # #     for i in range(idx,idx + len(gas)):
# # #         i = i % len(gas)
# # #         tank += gas[i]
# # #         if tank < cost[i]:
# # #             return -1
# # #         else:
# # #             tank = tank - cost[i]
# # #     return idx
# # # print(potd([6,5,6,6], [5,8,2,8]))

# # # default dictionary -- it doesn't raises Key Not Found Error
# # from collections import defaultdict
# # def groupAnagrams(strs):
# #     res = defaultdict(list)
# #     for s in strs:
# #         count = [0] * 26
# #         for c in s:
# #             count[ord(c)-ord("a")] += 1
# #         res[tuple(count)].append(s)
# #     return res.values()
# # print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))



# # """
# # lambda arguments: expression
# # """

# # # A most commmon returning style is:    return True if not stack else False



# # # def first(arr,idx,target):
# # #     if idx == len(arr) - 1:
# # #         return -1
    
# # #     if target == arr[idx]:
# # #         return idx
# # #     return first(arr, idx +  1, target)

# # # print(first([5,26,2,62,62,6,2,5], 0,50))
# # def last(arr,idx,target):
# #     # base case
# #     if idx == len(arr) :
# #         return -1 
    
# #     ans = last(arr, idx + 1, target)
# #     if ans == -1:
# #         if arr[idx] == target:
# #             return idx 
# #         else:
# #             return -1 
# #     else:
# #         return ans
# # print(last([5,26,2,62,62,6,2,5], 0,2))


# # def all(arr,idx,target,ans):
# #     # base case 
# #     if idx == len(arr):
# #         res = []
# #         return res 

# #     if arr[idx]  == target:
# #         ans += 1 
# #     iarr = all(arr, idx + 1 , target, ans)

# #     if arr[idx] == target:
# #         iarr.append(idx)
# #     return iarr

# # print(all([3,2,55,2,2,2,2,4], 0,2, 0))

# # def all(arr, idx,target):
# #     if idx == len(arr):
# #         res = []
# #         return res 
    
# #     if arr[idx ] == target:
# #         ans = all(arr, idx + 1, target)
# #         ans.append(idx)
# #         return ans
# #     else:
# #         ans = all(arr, idx+1, target)
# #         return ans

# # print(all([3,2,5,2,2,4], 0,2))


# # https://leetcode.com/problems/zigzag-conversion/
# # def convert(s,numRows):
# #     if numRows == 1:
# #         return s
# #     row_arr = [""] * numRows
# #     row_idx = 1
# #     going_up = True
# #     for ch in s:
# #         row_arr[row_idx-1] += ch
# #         if row_idx == numRows:
# #             going_up = False
# #         elif row_idx == 1:
# #             going_up = True
# #         if going_up:
# #             row_idx += 1
# #         else:
# #             row_idx -= 1
# #     return "".join(row_arr)
# # print(convert("PAYPALISHIRING", 3))


# def subsequence(s):
#     if len(s) == 0:
#         res = [""]
#         return res 
#     toAppend = s[:1]
#     remainining = s[1:]
#     res = subsequence(remainining)
#     ans = []
#     for c in res:
#         ele = "" + c 
#         ans.append(str(ele))
#     for c in res:
#         ele =  toAppend + c 
#         ans.append(str(ele))
#     return ans

# print(subsequence("abc"))

# # print(subsequence("abc"))

# """
# Chaining Technique

# """
# Longest Palindromic substring
"""
one more way to check for palindrome:
abcdefedcba
check the neighbouring the elements 
like check f ==f and then e == e and d == d and so on and expand outwards 

res = ""
reslen = 0
s = "baaaab"
for i in range(len(s)):
    # odd 
    l ,r = i ,i 
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r-l+1) > reslen:
            res = s[l:r+1]
            reslen = r - l + 1 
        l -= 1 
        r += 1
    # even
    l ,r = i ,i + 1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r-l+1) > reslen:
            res = s[l:r+1]
            reslen = r - l + 1 
        l -= 1 
        r += 1
print(res)

On negative remainder explanation -- I am thinking this way just to elaborate on it a bit ( have not seen Euclidean division)
21%5 = 1 , it means two things :

1 is extra, once removed, it would be divisible by 5 (ie. (21-1)%5 ==0)
it is short of 4, once added it would be divisible by 5 ( i.e. (21+4)%5 ==0)
so if you see -4 in the a previous sub-array sum, that previous sub-array is reducing the current total sum by "4"- the reason why current sum is short of 4.
So essentially, rem = "1" and "-4" is same thing, i.e. "21" is short of 4 for it to become divisible by 5 = "21" has extra "1" which when removed makes it divisible by 5.
"""