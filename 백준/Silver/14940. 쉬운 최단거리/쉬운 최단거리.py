
import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())
arr = []
result = [[0 for _ in range(M)] for _ in range(N)]
start = [-1,-1]

for i in range(N):
  input_line = list(map(int, sys.stdin.readline().split()))
  arr.append(input_line)
  if 2 in input_line:
    j = input_line.index(2)
    start = [i,j]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

queue = deque([start])

while queue:
  x, y = queue.popleft()
  count = result[x][y]

  for i in range(4):
    newX = x+dx[i]
    newY = y+dy[i]
    if 0 <= newX < N and 0 <= newY < M:
      if arr[newX][newY] == 1:
        result[newX][newY] = count+1
        #print(f"result[{newX}][{newY}: {count+1}]")
        arr[newX][newY] = 2
        queue.append([newX,newY])
      elif arr[newX][newY] == 0:
        result[newX][newY] = 0
  
for i in range(N):
  for j in range(M):
    if result[i][j] == 0:
      if arr[i][j] == 1:
        print(-1, end=" ")
      else: print(result[i][j], end=" ")
    else: print(result[i][j], end=" ")
  print()
