def solution(numbers):
    answer = []
    
    for idxi, i in enumerate(numbers):
        for idxj, j in enumerate(numbers):
            if i + j in answer:
                continue
            elif idxi == idxj:
                continue
            else:
                answer.append(i + j)
    answer.sort()
    return answer