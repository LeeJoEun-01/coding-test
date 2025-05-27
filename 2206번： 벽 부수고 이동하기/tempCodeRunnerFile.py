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

def bfs():
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
          else:
            if maze[newN][newM] == 1:
              if maze[n][m][1] == 0:
                count = maze[n][m][0] + 1
                maze[newN][newM] = [count, 1]
                queue.append([newN,newM])

  if maze[N-1][M-1] == 0:
    return -1
  else:
    return maze[N-1][M-1][0]+1

if (N*M)-len(indexOfWall) < N+M-2:
  print(-1)
else:
  print(bfs())