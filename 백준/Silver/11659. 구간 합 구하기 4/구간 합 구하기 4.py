import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
index_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

sum_arr = [0]
for i in range(N):
  sum_arr.append(sum_arr[i] + arr[i])

for index in index_arr:
  print(sum_arr[index[1]]-sum_arr[index[0]-1])