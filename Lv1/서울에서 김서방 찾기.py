def solution(seoul):
    n = 0
    for i in seoul:
        n += 1
        if i == 'Kim':
            return '김서방은 '+ str(n-1) +'에 있다'
    