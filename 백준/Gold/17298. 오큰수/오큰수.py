import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

stack = [0]
result = [-1]*N

for i in range(1, N):
  while stack and arr[stack[-1]] < arr[i]:
    result[stack.pop()] = arr[i]
  stack.append(i)

print(*result)