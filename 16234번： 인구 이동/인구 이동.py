#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16234                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16234                          #+#        #+#      #+#     #
#    Solved: 2025/03/08 16:09:30 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = []
for _ in range(N):
  line = list(map(int, input().split()))
  arr.append(line)

queue = deque([])
target = []
cnt = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      newX = x+dx[i]
      newY = y+dy[i]

      if 0 <= newX < N and 0 <= newY < N and visited[newX][newY] == 0:
        diff = abs(arr[x][y]-arr[newX][newY])
        if L <= diff <= R:
          visited[newX][newY] = 1
          queue.append([newX,newY])
          target.append([newX,newY])

while True:
  isDone = 0
  visited = [[0]*(N+1) for _ in range(N+1)]
  for i in range(N):
    for j in range(N):
      if visited[i][j] == 0:
        target = []
        visited[i][j] = 1
        queue.append([i,j])
        target.append([i,j])
        bfs()
        
        if len(target) > 1:
            isDone = 1
            avgVal = sum([arr[x][y] for x, y in target]) // len(target)
            for x,y in target:
                arr[x][y] = avgVal

  if isDone == 0:
    break
  
  cnt += 1

print(cnt)