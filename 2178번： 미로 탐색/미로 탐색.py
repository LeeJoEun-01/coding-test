#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2178                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2178                           #+#        #+#      #+#     #
#    Solved: 2024/08/10 16:54:37 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

n_direction = [-1,1,0,0] # 상,하,좌,우
m_direction = [0,0, -1, 1]

def bfs(n,m):
  queue = deque()
  queue.append([n,m])

  while queue:
    n, m = queue.popleft()

    for i in range(4):
      newN = n+n_direction[i]
      newM = m+m_direction[i]
      if newN >= 0 and newM >= 0 :
        if newN < N and newM < M:
          if maze[newN][newM] == 1:
            count = maze[n][m] + 1
            maze[newN][newM] = count
            queue.append([newN,newM])

  return maze[N-1][M-1]
  
print(bfs(0,0))
#print(maze)

# for i in maze:
#   for j in i:
#     print(j, end=" ")
#   print()
