import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
visited = [False]*(N+1)
result = []

def dfs():
  if len(result) == M:
    print(' '.join(map(str, result)))

  for i in range(1, N+1):
    if not visited[i]:
      visited[i] = True
      result.append(arr[i-1])
      dfs()
      result.pop()
      visited[i] = False

dfs()