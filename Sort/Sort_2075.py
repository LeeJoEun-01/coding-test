# Sort
# 2075. N번째로 큰 수

import sys

n = int(sys.stdin.readline())
list_2d = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

num_list = sum(list_2d, [])
num_list.sort(reverse=True)

print(num_list[n-1])
