import sys

N, T = map(int,sys.stdin.readline().split())

dp = [0]*(T+1)

for _ in range(N):
    K, S = map(int,sys.stdin.readline().split())
    for i in range(T, -1, -1):
        if i >= K:
            # print(f"=== i:{i} | K:{K} | S:{S}")
            # print(f"=== dp[i]: max({dp[i]}, {dp[i-K]+S})")
            dp[i] = max(dp[i], dp[i-K]+S)

print(dp[T])