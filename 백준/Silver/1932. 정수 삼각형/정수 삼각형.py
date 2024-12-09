import sys

n = int(sys.stdin.readline().rstrip())
dp = []
for _ in range(n):
  line = list(map(int, sys.stdin.readline().split()))
  dp.append(line)

for i in range(1,n):
  num = len(dp[i])

  for j in range(num):
    if j == 0:
      dp[i][j] += dp[i-1][0]
    elif j == num-1:
      dp[i][j] += dp[i-1][num-2]
    else:
      dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))