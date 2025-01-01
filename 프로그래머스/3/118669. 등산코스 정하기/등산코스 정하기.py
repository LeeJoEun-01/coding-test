import heapq
from math import inf

def solution(n, paths, gates, summits):
    result = []
    graph = [[] for _ in range(n+1)]
    for i in range(len(paths)):
        a, b, w = paths[i]
        graph[a].append([b,w])
        graph[b].append([a,w])

    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True

    distance = [inf]*(n+1)
    queue = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue,[0,gate])
        
    while queue:
        d, i = heapq.heappop(queue)
      # 산봉우리면 바로 continue
      # 이렇게 해야 두 개 이상의 산봉우리를 방문하지 않는다.
        if distance[i] < d or is_summit[i]:
            continue
        for j, dd in graph[i]:
            dd = max(distance[i], dd)
            if distance[j] > dd:
                distance[j] = dd
                heapq.heappush(queue, [dd, j])
    
    summits.sort()
    for summit in summits:
        result.append([summit, distance[summit]])
    
    result.sort(key=lambda x:(x[1],x[0]))
    answer = result[0]
    return answer