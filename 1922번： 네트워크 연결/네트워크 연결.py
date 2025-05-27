#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1922                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1922                           #+#        #+#      #+#     #
#    Solved: 2024/10/30 01:46:52 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import heapq

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
weight = 0

for i in range(M):
  v1, v2, w = map(int, sys.stdin.readline().split())
  graph[v1].append([w,v2])
  graph[v2].append([w,v1])

queue = []
heapq.heappush(queue, (0,1))

while queue:
  w, v = heapq.heappop(queue)
  if visited[v] == False:
    visited[v] = True
    weight += w
    for next_w, next_v in graph[v]:
      heapq.heappush(queue, (next_w, next_v))

print(weight)
