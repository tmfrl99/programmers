def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    
    for i in s:
        if i == i.upper() and i != ' ':
            answer += alpha[alpha.index(i.lower()) + n - 26].upper()
        elif i == i.lower() and i != ' ':
            answer += alpha[alpha.index(i.lower()) + n - 26]
        else:
            answer += ' '
    return answer