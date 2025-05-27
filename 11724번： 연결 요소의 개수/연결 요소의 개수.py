#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11724                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11724                          #+#        #+#      #+#     #
#    Solved: 2024/08/17 23:01:43 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]

for i in arr:
  graph[i[0]].append(i[1])
  graph[i[1]].append(i[0])

for i in graph:
  print(i)

def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

visited = [False] * (N+1)
count = 0

for i in range(1, N+1):
    if visited[i] == False:
      dfs(graph, i, visited)
      count += 1

print(count)