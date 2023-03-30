def length(s,idx):
    
    if idx == len(s):
        return 0
    
    return 1 + length(s, idx + 1 )

print(length("leetcode",0))

