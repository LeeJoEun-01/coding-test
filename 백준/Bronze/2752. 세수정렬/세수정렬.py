import sys

num_list = list((map(int, sys.stdin.readline().split())))

num_list.sort()

for i in num_list:
    print(i, end=" ")