#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1520                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1520                           #+#        #+#      #+#     #
#    Solved: 2025/05/17 16:43:06 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dp = [[-1]*M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if maps[x][y] > maps[nx][ny]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]


dfs(0, 0)
print(dp[0][0])
