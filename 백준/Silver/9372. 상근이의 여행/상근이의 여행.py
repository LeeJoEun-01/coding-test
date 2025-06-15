import sys
input = sys.stdin.readline

N = int(input().rstrip())
for _ in range(N):
    n, m = map(int, input().split())
    for _ in range(m):
        _ = input()
    print(n-1)