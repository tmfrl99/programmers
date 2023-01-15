def solution(n):
    answer = 0
    m = n
    while True:
        m += 1
        n_zero = str(bin(n))[2:].count('1')
        m_zero = str(bin(m))[2:].count('1')
        if n_zero == m_zero:
            break
    return m