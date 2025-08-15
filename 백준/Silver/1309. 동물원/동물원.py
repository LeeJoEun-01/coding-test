import sys
N = int(sys.stdin.readline().rstrip())

dp = [0]*(N)
dp[0] = 3

if N >= 2:
    dp[1] = 7

if N >= 3:
    for i in range(2, N):
        dp[i] = (dp[i-1]*2 + dp[i-2]) % 9901
print(dp[N-1])