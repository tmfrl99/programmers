def solution(n):
    fibo = [0, 1]
    if n == 2:
        return 1
    for i in range(2, n):
        fibo.append((fibo[i-2] + fibo[i-1]) % 1234567)
    return (fibo[n-2] + fibo[n-1]) % 1234567