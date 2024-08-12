import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

nd = [-1,1,0,0]
md = [0,0,-1,1]

def bfs():
  queue = deque()
  count = 0

  for i in range(N):
    for j in range(M):
      if tomatoes[i][j] == 1:
        queue.append([i,j])

  queue.append([-1,-1])

  while queue:
    n, m = queue.popleft()

    if n == -1 and m == -1:
      queue.append([-1,-1])
      n, m = queue.popleft()
      count += 1

    for i in range(4):
      newN = n+nd[i]
      newM = m+md[i]
      #print(f"newN:{newN}, newM:{newM}")
      if newN >= 0 and newM >= 0:
        if newN < N and newM < M:
          if tomatoes[newN][newM] == 0:
            tomatoes[newN][newM] = 1
            queue.append([newN,newM])
  
  for row in tomatoes:
    if 0 in row:
      return -1
      
  return count-1

print(bfs())