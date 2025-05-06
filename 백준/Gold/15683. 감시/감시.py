import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 왼, 아래, 오른, 위
dv = [[0, -1], [1, 0], [0, 1], [-1, 0]]
cctv_directions = {1: [[0], [1], [2], [3]],
                   2: [[0, 2], [1, 3]],
                   3: [[0, 1], [1, 2], [2, 3], [3, 0]],
                   4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
                   5: [[0, 1, 2, 3]]}
ans = 1e9

cctv = []
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            cctv.append((i, j, arr[i][j]))


def find_sight(maps, directions, x, y):
    for d in directions:
        nx = x
        ny = y

        while True:
            nx += dv[d][0]
            ny += dv[d][1]

            if 0 > nx or nx >= N or 0 > ny or ny >= M or maps[nx][ny] == 6:
                break
            elif maps[nx][ny] == 0:
                maps[nx][ny] = -1


def dfs(depth, maps):
    global ans

    if depth == len(cctv):
        count = 0
        for line in maps:
            count += line.count(0)
        ans = min(ans, count)
        return

    tmp_maps = copy.deepcopy(maps)
    x, y, n = cctv[depth]

    for directions in cctv_directions[n]:
        find_sight(tmp_maps, directions, x, y)
        dfs(depth+1, tmp_maps)
        tmp_maps = copy.deepcopy(maps)


dfs(0, arr)
print(ans)