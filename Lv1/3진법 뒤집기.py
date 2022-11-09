def solution(n):
    num = ''
    answer = 0
    while n > 0:
        n, m = divmod(n, 3)
        num += str(m)
    num = list(num)
    num.reverse()
    
    for i in range(len(num)):
        answer += 3**i*int(num[i])
    return answer
    # return int(num, 3)