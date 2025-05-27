#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1753                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1753                           #+#        #+#      #+#     #
#    Solved: 2024/10/17 17:33:24 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import math
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().strip())
graph = [[] for _ in range(V+1)]

for _ in range(E):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append((w,v))

weight = [math.inf]*(V)
weight[K-1] = 0
queue = []
heapq.heappush(queue, (0,K))

while queue:
  w, v = heapq.heappop(queue)

  if weight[v-1] < w:
    continue

  for newW, newV in graph[v]:
    if weight[newV-1] > w+newW:  
      weight[newV-1] = newW + w
      heapq.heappush(queue, (newW + w, newV))
  
for i in weight:
  if i == math.inf:
    print("INF")
  else:
    print(i)

  