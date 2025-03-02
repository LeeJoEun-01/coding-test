import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
  caseN, idx = map(int, sys.stdin.readline().split())
  arr = list(map(int, sys.stdin.readline().split()))

  for i in range(len(arr)):
    arr[i] = [i,arr[i]]
  
  queue = deque(arr)
  cnt = 0
  isDone = True

  if caseN == 1:
    print(1)
  else:
    while queue and isDone :
      # print(f"= {queue}")
      first = queue.popleft()

      for i in range(0, len(queue)):
        if first[1] < queue[i][1]:
          queue.append(first)
          break
        else:
          if i == len(queue)-1:
              cnt += 1
              if first[0] == idx:
                print(cnt)
                isDone = False
                break

    if isDone == True:
      print(cnt+1)