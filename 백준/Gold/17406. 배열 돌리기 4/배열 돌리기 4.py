import sys
from itertools import permutations
import copy
input = sys.stdin.readline

N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
copy_maps = []
rsc = [list(map(int, input().split())) for _ in range(K)]
nums = [i for i in range(K)]


result = []
for p in permutations(rsc, K):
    # 회전 연산
    copy_maps = copy.deepcopy(maps)
    for r, c, s in p:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):
            tmp = copy_maps[r-n][c+n]
            copy_maps[r-n][c-n+1:c+n+1] = copy_maps[r-n][c-n:c+n]  # ->
            for row in range(r-n, r+n):  # ↑
                copy_maps[row][c-n] = copy_maps[row+1][c-n]
            copy_maps[r+n][c-n:c+n] = copy_maps[r+n][c-n+1:c+n+1]  # <-
            for row in range(r+n, r-n, -1):  # ↓
                copy_maps[row][c+n] = copy_maps[row-1][c+n]
            copy_maps[r-n+1][c+n] = tmp

    min_val = 1e9
    for i in range(N):
        min_val = min(min_val, sum(copy_maps[i]))

    result.append(min_val)

print(min(result))