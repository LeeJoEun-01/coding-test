import sys

N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
arr.sort()

dp = [0]*(K+1)
dp[0] = 1

for n in arr:
    # dp[n] += 1
    for i in range(n,K+1):
      dp[i] += dp[i-n] 
  #print(dp)

print(dp[K])