def solution(n):
    answer, total = 1, 0
    num = int(n/2)
    for i in range(1, num+1):
        for j in range(i, num+2):
            total = sum(list(range(i, j+1)))
            if total > n:
                break
            elif total == n:
                answer += 1
                break
    return answer