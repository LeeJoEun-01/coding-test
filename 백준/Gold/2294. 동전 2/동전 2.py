import sys
from math import inf
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(int(input().rstrip()))

dp = [inf]*(K+1)
dp[0] = 0

for target in arr:
  for i in range(target,K+1):
      dp[i] = min(dp[i], dp[i-target]+1)

if dp[K] == inf:
  print(-1)
else:
  print(dp[K])