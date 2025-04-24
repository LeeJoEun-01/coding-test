def solution(nums):
    answer = 0
    pocket = {}
    N = len(nums)//2
    
    for n in nums:
        pocket.setdefault(n,0) 
        pocket[n] += 1
    
    if N <= len(pocket):
        answer = N
    else:
        answer = len(pocket)
        
    return answer