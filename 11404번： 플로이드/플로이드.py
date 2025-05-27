#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11404                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11404                          #+#        #+#      #+#     #
#    Solved: 2024/10/31 15:39:42 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import math

N = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
graph = [[math.inf for _ in range(N)] for _ in range(N)]

for i in range(B):
  v1, v2, w = map(int, sys.stdin.readline().split())
  if graph[v1-1][v2-1] > w:
    graph[v1-1][v2-1] = w

for k in range(N):
  for i in range(N):
    for j in range(N):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(N):
  for j in range(N):
    if i == j or graph[i][j] == math.inf:
      print(0, end=" ")
    else:
      print(graph[i][j], end=" ")
  print()
