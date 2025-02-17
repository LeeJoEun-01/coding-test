import sys
from math import inf
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input().rstrip())
input_arr = [list(map(int, input().split())) for _ in range(N)]
ans = inf
n = 0
tmp = []

def calc(arr):
  mul = 1
  add = 0
  for i, j in arr:
    mul *= i
    add += j
  return abs(mul-add)

def dfs(start, depth):
  global ans
  if depth == n:
    ans = min(ans, calc(tmp))
    return
  
  for i in range(start, N):
    tmp.append(input_arr[i])
    dfs(i+1, depth+1)
    tmp.pop()

for i in range(1,N+1):
  n = i
  dfs(0, 0)

print(ans)