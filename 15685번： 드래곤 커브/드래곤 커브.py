#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15685                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15685                          #+#        #+#      #+#     #
#    Solved: 2024/10/09 11:29:42 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# x,y: 시작 좌표 | d: 시작 방향 | g: 세대

import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

coordinates = []

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def dragonCurve(input):
  x, y = input[0], input[1]
  d = input[2]
  g = input[3]

  xy = [[x,y]]
  directions = [d]

  # 방향 배열 만들기
  for i in range(g):
    new = []

    for dd in reversed(directions):
      new_d = dd+1
      if new_d == 4:
        directions.append(0)
      else:
        directions.append(new_d)

  #방향 -> 좌표로 변환
  for i in directions:
    x = x+dx[i]
    y = y+dy[i]
    xy.append([x,y])
  
  return xy

def findRectangle(arr_xy):
  count = 0

  for target in arr_xy:
    if ([target[0], target[1]-1]) in arr_xy:
      if ([target[0]+1, target[1]-1]) in arr_xy:
        if ([target[0]+1, target[1]]) in arr_xy:
          count += 1

  return count


for line in arr:
  xy = dragonCurve(line)
  for i in xy:
    # 중복 제거
    if i not in coordinates:
      coordinates.append(i)

# coordinates.sort(key = lambda x: x[0])
print(findRectangle(coordinates))
