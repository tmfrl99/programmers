from itertools import combinations
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    lst = list(combinations(nums, 3))
    for i in lst:
        if is_prime(sum(i)):
            answer += 1
    return answer