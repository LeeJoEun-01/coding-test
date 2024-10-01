import sys

arr = list(str(sys.stdin.readline().rstrip()))
eStr = list(str(sys.stdin.readline().rstrip()))
num = len(eStr)

stack = []

for char in arr:
  stack.append(char)
  if stack[len(stack)-num:len(stack)+1] == eStr:
    for _ in range(num):
      stack.pop()

if len(stack) == 0:
  print("FRULA")
else:
  print("".join(stack))