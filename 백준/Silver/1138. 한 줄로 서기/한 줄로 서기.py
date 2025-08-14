import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [0] * n

for i, a in enumerate(arr):
    count = 0 
    for j, res in enumerate(result):
        if res == 0 and count < a:
            count += 1
        elif res == 0 and count == a:
            result[j] = i + 1
            break

print(*result)