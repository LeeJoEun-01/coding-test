from collections import deque

def solution(numbers, target):
    answer = 0
    sums = []
    dq = deque([0])
    
    for n in numbers:
        tmp_dp = deque()
        for d in dq:            
            add = d+n
            sub = d-n
            tmp_dp.append(add)
            tmp_dp.append(sub)
        dq = tmp_dp
    
    for d in dq:
        if d == target:
            answer += 1
            
    return answer