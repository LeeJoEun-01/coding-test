import sys

n = int(sys.stdin.readline().rstrip())
arr = [ int(sys.stdin.readline().rstrip()) for _ in range(n)]

dp = [0 for _ in range(n+1)]
dp[1] = arr[0]

if n >= 2:
  dp[2] = arr[0]+arr[1]
if n >= 3:
  dp[3] = max(arr[0]+arr[2], arr[1]+arr[2],dp[2])

for i in range(4, n+1):
  # print(f"=== {dp[i-2]+arr[i-1]}| {dp[i-3]+arr[i-2]+arr[i-1]}")
  dp[i] = max(dp[i-2]+arr[i-1], dp[i-3]+arr[i-2]+arr[i-1],dp[i-1])


print(max(dp))