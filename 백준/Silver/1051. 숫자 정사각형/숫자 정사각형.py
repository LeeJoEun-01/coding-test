
import sys
N, M = map(int, sys.stdin.readline().split())
square = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

ans = 0

for k in range(min(N, M), 0, -1):
    for i in range(N-k):
        for j in range(M-k):
            if square[i][j] == square[i][j+k] == square[i+k][j] == square[i+k][j+k]:
                ans = max(ans, k+1)

if ans != 0:
    print((ans)**2)
else:
    print(1)