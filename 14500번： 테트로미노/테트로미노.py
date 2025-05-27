#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14500                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14500                          #+#        #+#      #+#     #
#    Solved: 2024/11/06 21:00:28 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
  for j in range(M):
    arr[i][j] = arr[i][j]*-1
  
result = []

dx = [1,0,-1,0]
dy = [0,-1,0,1]

for i in range(N):
  for j in range(M):
    max_arr = []
    start = [i,j]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    queue = deque([start])
    num = 0

    while num<5:
      x, y = queue.popleft()

      for k in range(4):
        newX = x+dx[k]
        newY = y+dy[k]
        if i+4-7 <= newY < i+4 and j+4-7 <= newY < j+4 :
          if 0 <= newX <N and 0<= newY <M:
            if visited[newX][newY] == 0:
              queue.append([newX,newY])
              count = visited[x][y] + arr[newX][newY]
              visited[newX][newY] = count
              max_arr.append(count)
              num += 1
    
    result.append(min(max_arr))
  
print(result)
print(min(result))
