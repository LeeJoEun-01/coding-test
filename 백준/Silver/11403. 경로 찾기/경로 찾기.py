import sys

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for k in range(N): #중간
  for i in range(N): #시작
    for j in range(N): #끝
      if graph[i][j] == 1 or graph[i][k]+graph[k][j] == 2:
        graph[i][j] = 1

for line in graph:
  print(*line)