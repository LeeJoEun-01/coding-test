import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]

graph = [[] for _ in range(N+1)]
for x, y in tree:
  graph[x].append(y)
  graph[y].append(x)

parent = [ 0 for _ in range(N+1)]

queue = deque([1])
parent[1] = 0

while queue:
  node = queue.pop()

  for i in graph[node]:
    if parent[i] == 0:
      parent[i] = node
      queue.append(i)

for i in range(2,N+1):
  print(parent[i])