import sys
from math import inf
input = sys.stdin.readline

N = int(input().rstrip())

if N >=2 :
  dp = [inf]*(N+1)
  dp[0] = 0
  dp[1] = 0

  for i in range(2, N+1):
    if i%2 == 0 and i%3 == 0:
      dp[i] = min(dp[i//2], dp[i//3], dp[i-1])+1
    elif i%2 == 0:
      dp[i] = min(dp[i//2], dp[i-1])+1
    elif i%3 == 0:
      dp[i] = min(dp[i//3], dp[i-1])+1
    else:
      dp[i] = dp[i-1]+1
  # print(dp)
  print(dp[N])
else:
  print(0)