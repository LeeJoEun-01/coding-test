
import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [0]*(N+1)
dp[3] = 1
if N >= 5:
    dp[5] = 1

for i in range(6, N+1):
    if N >= 5:
        if dp[i-3] != 0 and dp[i-5] != 0:
            dp[i] = min(dp[i-3]+1, dp[i-5]+1)
        elif dp[i-3] != 0:
            dp[i] = dp[i-3]+1
        elif dp[i-5] != 0:
            dp[i] = dp[i-5]+1
        else:
            dp[i] = 0
    else:
        if dp[i-3] != 0:
            dp[i] = dp[i-3]+1
        else:
            dp[i] = 0

# print(dp)

if dp[N] == 0:
    print(-1)
else:
    print(dp[N])