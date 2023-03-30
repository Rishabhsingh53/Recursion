def solution(s,idx):
    
    if idx == len(s):
        return ""

    if ord(s[idx]) >= 65 and ord(s[idx]) <= 90:
        return s[idx]
    return solution(s, idx + 1 )

s = "geeksForgeeks"
print(solution(s,0))