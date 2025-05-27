# Sort
# 11399. ATM

import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()

sum = 0
for i in range(n+1):
    for j in range(i):
        sum += num_list[j]

print(sum)
