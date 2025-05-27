#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11725                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11725                          #+#        #+#      #+#     #
#    Solved: 2024/08/15 14:01:10 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]

graph = [[] for _ in range(N+1)]
for x, y in tree:
  graph[x].append(y)
  graph[y].append(x)

parent = [ 0 for _ in range(N+1)]

queue = deque([1])
parent[1] = 0

while queue:
  node = queue.pop()

  for i in graph[node]:
    if parent[i] == 0:
      parent[i] = node
      queue.append(i)

for i in range(2,N+1):
  print(parent[i])