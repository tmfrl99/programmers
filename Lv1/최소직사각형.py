def solution(sizes):
    maxb, mins = 0, 0
    
    for i in range(len(sizes)):
        big = sizes[i][0]
        small = sizes[i][1]
        
        if small > big:
            w = big
            big = small
            small = w
            
        if big > maxb:
            maxb = big
            
        if small > mins:
            mins = small
            
    return maxb*mins