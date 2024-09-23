import sys

A = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

result = [1 for _ in range(A)]

for i in range(1,A):
  for j in range(0,i):
    if arr[j] < arr[i]:
      result[i] = max(result[i], result[j]+1)

print(max(result))