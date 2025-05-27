# DFS
# 1012. 유기농 배추
import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 상, 하, 좌, 우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안에 있고 1이면(=배추이면) 지나간것을 -1로 표시하고 주변 탐색
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)


t = int(sys.stdin.readline())
result = []
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    # 배추 위치 표시
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1  # x, y 반대로 들어가는거 주의 !!

    # 배추흰지렁이 개수 세기
    count = 0
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                dfs(x, y)
                count += 1
    print(count)

#     result.append(count)

# for i in result:
#     print(i)
