#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18352                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18352                          #+#        #+#      #+#     #
#    Solved: 2024/10/16 12:37:23 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import math
import heapq

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
distance = [math.inf]*N

answer = []
distance[X-1] = 0

for _ in range(M):
  a, b = map(int,sys.stdin.readline().split())
  graph[a].append(b)

queue = []
heapq.heappush(queue, (0, X))

while queue:
  dist, index = heapq.heappop(queue)

  if distance[index-1] < dist:
    continue

  for i in graph[index]:
    cost = dist+1
    if cost < distance[i-1]:
      distance[i-1] = cost
      heapq.heappush(queue, (cost, i))
  
flag = 0

for i in range(N):
  if distance[i] == K:
    print(i+1)
    flag = 1

if flag == 0:
  print(-1)
