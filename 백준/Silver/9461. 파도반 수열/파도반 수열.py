import sys
input = sys.stdin.readline

T = int(input().rstrip())
inputs = []

for _ in range(T):
    N = int(input().rstrip())
    inputs.append(N)

maxN = max(inputs)

dp = [0]*(maxN)
dp[0], dp[1], dp[2] = 1, 1, 1

for i in range(3, maxN):
    dp[i] = dp[i-2]+dp[i-3]

for n in inputs:
    print(dp[n-1])
