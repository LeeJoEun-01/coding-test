import sys

N = int(sys.stdin.readline().rstrip())

start = 2
cnt = 1
term = 0

while N >= start:
  term += 6
  start += term
  cnt += 1

print(cnt)