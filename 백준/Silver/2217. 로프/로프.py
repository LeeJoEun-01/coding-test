import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(N)]
arr.sort()

ans = 0
for i in range(N):
    tmp = arr[i]*(N-i)
    if tmp > ans:
        ans = tmp
print(ans)