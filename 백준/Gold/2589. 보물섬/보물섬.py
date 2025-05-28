import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(N)]
ans = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

deq = deque([])
visited = []


def bfs():
    count = 0
    while deq:
        x, y, c = deq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == "L" and visited[nx][ny] == 0:
                    deq.append([nx, ny, c+1])
                    visited[nx][ny] = 1
                    if count < c+1:
                        count = c+1
    return count


for i in range(N):
    for j in range(M):
        if maps[i][j] == "L":
            visited = [[0 for _ in range(M)] for _ in range(N)]
            visited[i][j] = 1
            deq.append([i, j, 0])
            count = bfs()
            if ans < count:
                ans = count
print(ans)