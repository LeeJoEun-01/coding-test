import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
  commands = list(sys.stdin.readline().rstrip())
  n = int(sys.stdin.readline().rstrip())
  arr = sys.stdin.readline().rstrip()[1:-1].split(",")

  if n == 0:
    arr = []

  start = 0
  queue = deque(arr)
  result = True
  rCount = 0

  for command in commands:
    if command == 'R':
      rCount += 1
    elif command == 'D':
      if queue:
        if rCount%2 == 0:
          queue.popleft()
          rCount = 0
        else:
          queue.pop()
          rCount = 1
      else:
        result = False
        #break
  
  if rCount%2 != 0:
    queue.reverse()

  #answer = queue
  if result == False :
    print("error")
  else:
    print("[" + ",".join(queue) + "]")
