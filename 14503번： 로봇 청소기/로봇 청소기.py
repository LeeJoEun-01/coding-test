#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14503                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14503                          #+#        #+#      #+#     #
#    Solved: 2024/12/26 20:25:04 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

N, M = map(int, sys.stdin.readline().split())
start_x, start_y, start_d = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

x = start_x
y = start_y
d = start_d
count = 0
isDone = True

while isDone :
  if arr[x][y] == 0:
    arr[x][y] = 2
    count += 1
  
  isBlank = False
  # 주변에 청소되지 않은 빈 방이 있는지 확인
  for i in range (4):
    newX = x+dx[i]
    newY = y+dy[i]

    if 0 <= newX < N and 0<= newY < M:
      if arr[newX][newY] == 0:
        isBlank = True
        break
  
  if isBlank: # 청소할 방이 있는 경우
    for i in range(4):
      # count += 1
      d = d-1 if d != 0 else 3 # 90도 회전

      newX = x+dx[d]
      newY = y+dy[d]
      if 0 <= newX < N and 0<= newY < M:
        if arr[newX][newY] == 0:
          x = newX
          y = newY
          break

  else: # 청소할 방이 없는 경우
    newD = d+2 if d == 0 or d == 1 else d-2
    newX = x+dx[newD]
    newY = y+dy[newD]

    if 0 <= newX < N and 0<= newY < M:
      if arr[newX][newY] == 1:
        isDone = False
      else:
        x = newX
        y = newY

print(count)