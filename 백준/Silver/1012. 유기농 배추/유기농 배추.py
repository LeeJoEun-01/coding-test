import sys
from collections import deque

def bfs(graph, visited):
  count = 0
  while False in visited:
    for i in range(len(visited)):
      if visited[i] == False:
        count += 1
        start = i
        queue = deque([start])
        visited[start] = True
        break

    while queue:
      v = queue.popleft()

      for i in graph[v]:
        if not visited[i]:
          queue.append(i)
          visited[i] = True
  return count

def convertGraph(arr):
  result = []
  for i in range(len(arr)):
    result.append([])
    target = arr[i]    
    for j in range(len(arr)):
      if abs(target[0] - arr[j][0]) == 1 and target[1] == arr[j][1]:
        result[i].append(j)
      elif abs(target[1] - arr[j][1]) == 1 and target[0] == arr[j][0]:
        result[i].append(j)
  return result

T = int(sys.stdin.readline()) # 테스트케이스

for i in range(T):
  M, N, K = map(int, sys.stdin.readline().split()) # 가로, 세로, 배추가 심어져 있는 개수
  arr = []
  for _ in range(K):
    v = list(map(int, sys.stdin.readline().split()))
    arr.append(v)
  graph = convertGraph(arr)
  visited = [False]*K
  count = bfs(graph, visited)
  print(count)