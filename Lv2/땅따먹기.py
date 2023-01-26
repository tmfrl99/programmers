def solution(land): 
    answer = []
    for i in range(1, len(land)): 
        for j in range(4):
            temp = land[i-1][j] 
            land[i-1][j] = -1
            land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][2], land[i-1][3])
            land[i-1][j] = temp
        answer = max(land[i][0], land[i][1], land[i][2], land[i][3])
        
    return answer