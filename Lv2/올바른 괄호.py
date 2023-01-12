def solution(s):
    stack = list(s)
    sum = 0
    
    for i in stack:
        if i == "(":
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            return False
    
    if sum == 0:
        return True
    else:
        return False