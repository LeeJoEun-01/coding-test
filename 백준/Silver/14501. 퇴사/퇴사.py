import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*(N+1)

for i in range(1, N+1):
    d, w = arr[i-1]
    if i+d-1 <= N:
        # print(f"== {d+i-1}: max({dp[d+i-1]}, {dp[i-1]+w}, {w})")
        dp[d+i-1] = max(dp[d+i-1], dp[i-1]+w, w)

    dp[i] = max(dp[i], dp[i-1])

print(max(dp))