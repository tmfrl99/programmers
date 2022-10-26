def solution(n):
    li = list(str(n))
    li.sort(reverse=True)
    answer = ""
    for i in li:
        answer += str(i)
    return int(answer)