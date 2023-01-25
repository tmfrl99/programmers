def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    size_count = {}
    
    for i in tangerine:
        if i in size_count:
            size_count[i] += 1
        else:
            size_count[i] = 1
            
    size_count = dict(sorted(size_count.items(), key=lambda x: x[1], reverse=True))

    for i in size_count:
        if k <= 0:
            return answer
        k -= size_count[i]
        answer += 1
    return answer