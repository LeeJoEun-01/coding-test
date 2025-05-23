import sys
N, K = map(int, sys.stdin.readline().split())

nums = [0]*(N+1)
count = 0

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if nums[j] == 0:
            count += 1
            nums[j] = 1
            if count == K:
                print(j)