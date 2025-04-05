import sys
input = sys.stdin.readline

N = int(input().strip())

skyline = []
for _ in range(N):
  x, y = map(int, input().split())
  skyline.append(y)
skyline.append(0)

cnt = 0
arr = [0]
for h in skyline:
  height = h
  while arr[-1] > h:
    if arr[-1] != height:
      cnt += 1
      height = arr[-1]
    arr.pop()
  arr.append(h)

print(cnt)