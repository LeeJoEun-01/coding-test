import sys
import math

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

result = [0, 0, 0]
answer = float("inf")

for i in range(N-2):
  start = i
  mid = i+1
  end = N-1

  while mid < end:
    sum = arr[start]+arr[mid]+arr[end]

    if abs(sum) < answer:
      answer = abs(sum)
      # print(f"sum: {sum}")
      result = [arr[start], arr[mid], arr[end]]
      
    if sum > 0:
        end -= 1
    elif sum < 0:
        mid += 1
    else:
      break


print(result[0], result[1], result[2])
