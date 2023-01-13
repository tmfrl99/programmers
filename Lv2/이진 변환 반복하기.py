def solution(s): 
    answer = []
    zero, count = 0, 0
    while s != '1':
        zero += s.count('0')
        s = s.replace('0', '')  
        s = bin(len(s))[2:]
        count += 1
    answer = [count, zero]
    return answer