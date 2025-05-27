#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2206                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2206                           #+#        #+#      #+#     #
#    Solved: 2024/08/12 11:18:19 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

indexOfWall = []
for i in range(N):
  for j in range(M):
    if maze[i][j] == 1:
      indexOfWall.append([i,j])

nd = [-1,1,0,0]
md = [0,0,-1,1]

maze[0][0]=[0,0]

def bfs(num):
  queue = deque()
  queue.append([0,0])

  while queue:
    n, m = queue.popleft()

    for i in range(4):
      newN = n+nd[i]
      newM = m+md[i]
      if newN >= 0 and newM >= 0:
        if newN < N and newM < M:
          if maze[newN][newM] == 0:
            maze[newN][newM] = [maze[n][m][0] + 1, maze[n][m][1]]
            queue.append([newN,newM])
          elif maze[newN][newM] == 1:
            if maze[n][m][1] == 0:
              maze[newN][newM] = [maze[n][m][0] + 1, maze[n][m][1]+1]
              queue.append([newN,newM])
          else: ## 이미 인덱스가 3자리라면?
            count = maze[n][m][0] + 1
            break_wall = maze[n][m][1] + maze[newN][newM][1]
            if num == 1:
              if maze[newN][newM][0] >= count and maze[n][m][1] == 0:
                maze[newN][newM] = [count,0]
            elif num == 2:
              if maze[n][m][1] == 0:
                maze[newN][newM] = [count,0]


    print(f"=== maze[{n}][{m}] ===")
    for row in maze:
      print(row)

  if maze[N-1][M-1] == 0:
    return -1
  else:
    return maze[N-1][M-1][0]+1

if N == 1 and M == 1:
  print(1)
elif (N*M)-len(indexOfWall) < N+M-2:
  print(-1)
else:
  result = bfs(1)
  if result == -1:
    result = bfs(2)
  print(result)