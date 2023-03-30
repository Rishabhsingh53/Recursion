# Function for generating all subsequence of a string
def subseq(string,ans) -> list[str]:
    # base condition 
    if len(string) == 0:
        return [""]
    
    first = string[0]
    rest = string[1:]

    res = subseq(rest, ans)
    
    temp = []

    for i in res:
        temp.append("" + i)
        temp.append(first  + i)
    
    return temp

print(subseq("abc", []))
