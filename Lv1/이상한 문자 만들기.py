def solution(s):
    s = s.split(' ')
    word = ''
    for i in s:
        for w in range(len(i)):
            if w % 2 == 0:
                word += i[w].upper()
            else:
                word += i[w].lower()
        word += ' '
    return word[0:-1]