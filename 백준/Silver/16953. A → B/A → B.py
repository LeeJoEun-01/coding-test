import sys

input = sys.stdin.readline()
A, B = map(int, input.split())
count = 1

while B > A:
  if B%2 == 0:
    B = B//2
    count += 1
  else:
    if (B-1)%10 == 0:
      B = (B-1)//10
      count += 1
    else:
      break
  # print(B)

if B == A:
  print(count)
else:
  print(-1)