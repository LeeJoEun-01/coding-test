import sys

N = int(sys.stdin.readline().rstrip())

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1

for i in range(N):
    if i >= 2:
        dp[i] = dp[i-1]+dp[i-2]

print(dp[N-1])