def solution(left, right):
    res = 0
    for n in range(left, right+1):
        cnt = 0
        for i in range(1, n):
            if n % i == 0:
                cnt += 1
        if cnt % 2 != 0:
            res += n
        else:
            res -= n
    return res