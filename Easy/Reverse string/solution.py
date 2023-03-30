def reverse(s,idx):
    
    if idx == len(s) - 1:
        return s[idx]
    
    res = reverse(s, idx+1)

    ans = ""
    ans = res + s[idx]

    return ans 

print(reverse("leetcode",0))