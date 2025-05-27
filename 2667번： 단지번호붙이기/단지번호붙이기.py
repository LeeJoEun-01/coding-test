#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2667                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2667                           #+#        #+#      #+#     #
#    Solved: 2025/02/26 20:24:20 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(input().rstrip()) for _ in range(N)]
house = []

for i in range(N):
  for j in range(N):
    if arr[i][j] == '1':
      house.append([i,j])

visited = [[ False for _ in range(N) ]for _ in range(N)]
queue = deque()

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs():
  cnt = 0
  
  while queue:
    x, y = queue.pop()

    for i in range(4):
      newX = x+dx[i]
      newY = y+dy[i]

      if 0 <= newX < N and 0 <= newY < N:
        if arr[newX][newY] == '1' and visited[newX][newY] == False:
          cnt +=1
          visited[newX][newY] = True
          queue.append([newX, newY])
  return cnt

result = []

for x, y in house:
  if visited[x][y] == False:
    queue.append([x, y])
    result.append(dfs())

result.sort()
print(len(result))
for re in result:
  if re == 0:
    print(1)
  else: print(re)

