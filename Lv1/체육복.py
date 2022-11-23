def solution(n, lost, reserve):
    lost_lst = [i for i in lost if i not in reserve]
    reverse_lst = [i for i in reserve if i not in lost]
    lost_lst.sort()
    reverse_lst.sort()
    answer = n - len(lost_lst)
    for i in lost_lst:
        if i-1 in reverse_lst:
            answer += 1
            reverse_lst.remove(i-1)
        elif i+1 in reverse_lst:
            answer += 1
            reverse_lst.remove(i+1)
    return answer