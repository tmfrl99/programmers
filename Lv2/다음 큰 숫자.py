def solution(n):
    answer = 0
    m = n
    n_zero = bin(n).count('1')
    while True:
        m += 1
        m_zero = bin(m).count('1')
        if n_zero == m_zero:
            break
    return m