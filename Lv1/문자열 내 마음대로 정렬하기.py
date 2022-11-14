def solution(strings, n):
    lst = []
    res = []
    for i in strings:
        lst.append(i[n]+i)
    lst.sort()
    
    for i in lst:
         res.append(i[1:])

    return res