import sys

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
input = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
  for j in range(N):
    dp[i+1][j+1] = dp[i+1][j]+ dp[i][j+1]-dp[i][j] + arr[i][j]

# print(arr)

for line in input:
  x1, y1 = line[0], line[1]
  x2, y2 = line[2], line[3]

  print(dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])