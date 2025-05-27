#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14442                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14442                          #+#        #+#      #+#     #
#    Solved: 2024/11/20 01:09:16 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append([0,0,K])
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs():
  queue = deque()
  queue.append([0,0,K])
  
  while queue:
    print(f"=== queue: {queue}")
    x, y, z = queue.popleft()
    if x == N-1 and y == M-1:
      return visited[x][y][z]+1

    for i in range(4):
      newX = x+dx[i]
      newY = y+dy[i]

      if 0<= newX < N and 0<= newY < M:
        if arr[newX][newY] == 1 and visited[newX][newY][z-1] == 0 and z > 0:
            visited[newX][newY][z-1] = visited[x][y][z]+1
            queue.append([newX, newY, z-1])
        elif arr[newX][newY] == 0 and visited[newX][newY][z] == 0:
            visited[newX][newY][z] = visited[x][y][z]+1
            queue.append([newX, newY, z])
    
    print("==== visited =====")
    print(visited)
    
  return -1

print(bfs())
          





