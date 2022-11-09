def solution(d, budget):
    res = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            res += 1
            budget -= d[i]
        else:
            break
    return res