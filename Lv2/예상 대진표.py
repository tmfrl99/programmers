import math
def solution(n,a,b):
    answer = 0
    while True: 
        if a == b or a == 0 or b == 0:
            break
        a = math.ceil(a/2) 
        b = math.ceil(b/2) 
        answer += 1 
    return answer