def solution(phone_number):
    lst = list(map(str, phone_number))
    for i in range(len(lst)-4):
        lst[i] = "*"
    return str("".join(lst))