def solution(x):
    n = x
    s = 0
    while n > 0: 
        s += n % 10
        n //= 10
    if x % s == 0:
        return True
    else:
        return False