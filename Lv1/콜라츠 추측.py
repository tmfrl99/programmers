def solution(num):
    res = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        res += 1
        if res >= 500:
            return -1
    return res