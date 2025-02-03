import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [-1]*(N+1)

def fib(n):
  if dp[n] != -1:
    return dp[n]
  else:
    return fib(n-1)+fib(n-2)

dp[0] = 0
dp[1] = 1

for i in range(2,N+1):
  dp[i] = fib(i)

print(dp[N])