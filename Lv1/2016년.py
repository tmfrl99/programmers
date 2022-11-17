def solution(a, b):
    week_list = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    
    for i in range(a-1):
        days += day_list[i]
    days += b - 1  
    days %= 7
        
    return week_list[days]