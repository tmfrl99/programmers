def solution(s):
    s_list = list(s)
    words = s.split(' ')
    for i in range(len(words)):
        if words[i] == '':
            continue
        else:
            words[i] = words[i][0].upper() + words[i][1:].lower()
    return ' '.join(words)