#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1043                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1043                           #+#        #+#      #+#     #
#    Solved: 2024/12/30 01:45:38 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# import sys

# N, M = map(int, sys.stdin.readline().rstrip().split())
# truth = list(map(int, sys.stdin.readline().rstrip().split()))
# party = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
# result = []

# def find(parent,x):
#   if x != parent[x]:
#     parent[x] = find(parent, parent[x])
#   return parent[x]

# def union(parent,a,b):
#   a = find(parent,a)
#   b = find(parent,b)
  
#   if a<b:
#     parent[b]=a
#   else:
#     parent[a]=b

# parent = [i for i in range(N+1)]
# count = M

# if truth[0] == 0:
#   print(M)
# else:
#   del truth[0]
#   truth = set(truth)

#   for i in range(M):
#     arr = sorted(party[i][1:])
#     for j in range(1,len(arr)):
#       if find(parent, arr[0]) != find(parent, arr[j]):
#         union(parent, arr[0],arr[j])
    
#   visited = [0]*(N+1)
#   for i in range(1, N+1):
#     if i in truth and not visited[i]:
#       p = find(parent,i) 
#       for j in range(1, N+1):
#         if find(parent,j) == p:
#           visited[j] = 1
#           truth.add(j)
  
#   for i in range(M):
#     for j in range(1, party[i][0]+1):
#       if party[i][j] in truth:
#         count -= 1
#         break
#   print(count)

import heapq
from math import inf

def solution():
    n = 6
    paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
    gates = [1,3]
    summits = [5]	

    result = []
    graph = [[] for _ in range(n+1)]
    for i in range(len(paths)):
        a, b, w = paths[i]
        graph[a].append([b,w])
        graph[b].append([a,w])
    
    distance = [inf]*(n+1)
    queue = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue,[0,gate])

    isSummit = [False]*(n+1)
    for summit in summits:
        isSummit[summit] = True
        
    while queue:
        dist, i = heapq.heappop(queue)
        if distance[i] >= dist and not isSummit[i]:
            print(f"===dist:{dist} | i:{i}")
            for j in graph[i]:
                print(f"j: {j}")
                newDist = max(distance[i], j[1])
                if distance[j[0]] > newDist:
                    distance[j[0]] = newDist
                    heapq.heappush(queue,[newDist, j[0]])
        print(distance)

    summits.sort()
    for summit in summits:
        result.append([summit, distance[summit]])
    
    result.sort(key=lambda x:(x[1],x[0]))
    answer = result[0]
    return answer

print(solution())