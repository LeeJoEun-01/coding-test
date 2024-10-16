import sys
import math
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
result = [math.inf]*N
visited = [False]*N

answer = []
result[X-1] = 0
visited[X-1] = True

for _ in range(M):
  a, b = map(int,sys.stdin.readline().split())
  graph[a].append(b)

queue = deque([X])

while queue:
  index = queue.popleft()

  for i in graph[index]:
    if not visited[i-1]:
      visited[i-1] = True
      result[i-1] = result[index-1]+1
      queue.append(i)
      if result[i-1] == K:
        answer.append(i)

if len(answer) != 0:
  answer.sort()
  for i in answer:
    print(i)
else:
  print(-1)