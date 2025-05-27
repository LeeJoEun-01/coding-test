# import sys

# n = int(input())
# num_list = list(map(int, input().split()))
# v = int(input())

# print(num_list.count(v))

n = int(input())

for i in range(n, 0, -1):
    print(" "*(n-i), end="")
    print("*"*(i))
