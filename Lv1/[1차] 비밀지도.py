def solution(n, arr1, arr2):
    two1 = [[0 for j in range(n)] for i in range(n)]
    two2 = [[0 for j in range(n)] for i in range(n)]
    answer = [0] * n
    
    for idx, i in enumerate(arr1):
        for j in range(len(arr1)):
            i, m = divmod(i, 2)
            two1[idx][j] = m
        two1[idx].reverse()
        
    for idx, i in enumerate(arr2):
        for j in range(len(arr2)):
            i, m = divmod(i, 2)
            two2[idx][j] = m
        two2[idx].reverse()
        
    for i in range(len(two1)):
        res = ''
        for j in range(len(two2)):
            if two1[i][j] == 1 or two2[i][j] == 1:
                res += '#'
            else:
                res += ' '
        answer[i] = res
    return answer