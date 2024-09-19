
import sys

N, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, K+1):
    if arr[i-1][0] > j:
      dp[i][j] = dp[i-1][j]
    else :
      # print(f"j: {j} | arr[i][0]: {arr[i-1][0]}")
      # print(f"j-arr[i][0]: {j-arr[i-1][0]} | dp[i-1][j-arr[i][0]]: {dp[i-1][j-arr[i-1][0]]}")
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1][0]] + arr[i-1][1])


print(dp[N][K])