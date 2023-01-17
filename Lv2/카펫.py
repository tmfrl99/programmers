def solution(brown, yellow):
    answer = []
    ydivisor = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            ydivisor.append(i) 

    ylen = len(ydivisor) 
    for i in range(ylen): 
        if (ydivisor[i]+ydivisor[ylen-1])*2+4 == brown:
            answer.append(ydivisor[ylen-1]+2)
            answer.append(ydivisor[i]+2)
            break
        ylen -= 1
    return answer