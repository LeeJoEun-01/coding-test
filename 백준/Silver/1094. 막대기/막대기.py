
import sys
input = sys.stdin.readline

N = int(input().rstrip())

before = 1
tmp = 1
arr = [0]*(N+1)

while tmp <= N:
  for i in range(1,tmp):
    if arr[i] != 0 and i+tmp <= N:
      # print(f"=== arr[{i+tmp}] = {arr[i]+1}")
      arr[i+tmp] = arr[i]+1
  arr[tmp] = 1
  before = tmp
  tmp *= 2

print(arr[N])