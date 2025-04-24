import heapq

def solution(scoville, K):
    answer = 0
    h = []#heapq.heapify(scoville)
    for s in scoville:
        heapq.heappush(h,s)
    
    while True:
        if len(h) <= 1:
            end = heapq.heappop(h)
            if end < K:
                answer = -1
            break
            
        a = heapq.heappop(h)
        if a >= K:
            break
        b = heapq.heappop(h)
        answer += 1
        
        heapq.heappush(h, a+(b*2))
        
    return answer