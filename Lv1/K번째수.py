def solution(array, commands):
    lst = []
    answer = []
    
    for i in range(len(commands)):
        lst = array[commands[i][0]-1:commands[i][1]]
        lst.sort()
        answer.append(lst[commands[i][2]-1])
    return answer