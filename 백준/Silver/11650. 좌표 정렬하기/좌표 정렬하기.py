import sys

n = int(sys.stdin.readline())

num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

num_list.sort()

for nums in num_list:
    for num in nums:
        print(num, end=" ")
    print()