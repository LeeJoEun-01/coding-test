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
    #arr[i][j] = 0

dx = [1,0,-1,0]
dy = [0,-1,0,1]

queue = deque([start])

while queue:
  x, y = queue.popleft()
  count = result[x][y]
  if count == 0:
    count = -2

  for i in range(4):
    newX = x+dx[i]
    newY = y+dy[i]
    if 0 <= newX < N and 0 <= newY < M:
      if arr[newX][newY] == 1:
        result[newX][newY] = count+1
        arr[newX][newY] = 2
        queue.append([newX,newY])
      elif arr[newX][newY] == 0:
        result[newX][newY] = 0
  
for line in result:
  print(*line)
