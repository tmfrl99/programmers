def solution(n):
    i = 0
    while True:
        i += 1
        if n % i == 1:
            break
    return i