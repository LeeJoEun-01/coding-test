
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
dp = arr

for i in range(len(arr)):
    for j in range(0, i):
        dp[i] = max(dp[i-j-1]+dp[j], dp[i])

print(dp[N-1])