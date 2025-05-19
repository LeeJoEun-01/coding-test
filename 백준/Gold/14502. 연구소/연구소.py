import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 벽을 세울 수 있는 조합을 백트랙킹으로 만들고
# BFS로 바이러스 수 세기

safe_max = 0
block = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

virus = []
start = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            virus.append([i, j])


def bfs():
    tmp = [row[:] for row in maps]
    for x, y in block:
        tmp[x][y] = 1

    deq = deque()
    for x, y in virus:
        deq.append([x, y])

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    deq.append([nx, ny])

    count = 0
    for line in tmp:
        count += line.count(0)
    return count


def backTracking():
    global safe_max

    if len(block) == 3:
        num = bfs()
        if safe_max < num:
            safe_max = num
        return

    for i in range(N):
        for j in range(M):

            if maps[i][j] == 0 and [i, j] not in block:
                block.append([i, j])
                maps[i][j] = 1
                backTracking()
                block.pop()
                maps[i][j] = 0


backTracking()
print(safe_max)
