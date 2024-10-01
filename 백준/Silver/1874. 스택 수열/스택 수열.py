import sys

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

start = 1
stack = []
result = []

def answer():
  global start
  for i in range(N):
    if len(stack) == 0 or stack[-1] < arr[i]:
      for j in range(start, arr[i]+1):
        stack.append(j)
        result.append("+")
      start = arr[i]+1
    
    if stack[-1] == arr[i]:
      stack.pop()
      result.append("- ")
    else:
      print("NO")
      return
  for i in result:
    print(i)
  return

answer()