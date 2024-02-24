import sys

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

num_list.sort()

for i in num_list:
    print(i)