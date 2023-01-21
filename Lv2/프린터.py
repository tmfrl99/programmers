def solution(priorities, location):
    answer = 0
    max_p = max(priorities)
    while True:
        for i in range(len(priorities)):
            if max_p == priorities[i]:
                answer += 1 
                priorities[i] = 0 
                max_p = max(priorities) 
                if i == location:
                    return answer