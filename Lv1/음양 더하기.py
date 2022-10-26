def solution(absolutes, signs):
    sum = 0
    for idx, i in enumerate(absolutes):
        if signs[idx] == True:
            sum += i
        else:
            sum -= i
    return sum