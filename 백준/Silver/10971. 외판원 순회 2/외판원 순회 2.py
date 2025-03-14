import sys
input = sys.stdin.readline
from math import inf

N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
ans = inf

def dfs(v, depth, w):
  global ans

  if depth == N-1:
    if arr[v][0] != 0:
      if w+arr[v][0] < ans:
        ans = w+arr[v][0]
    return

  for i in range(1,N):
    if visited[i] == 0 and arr[v][i] != 0:
      visited[i] = 1
      dfs(i, depth+1, w+arr[v][i])
      visited[i] = 0

dfs(0,0,0)
print(ans)