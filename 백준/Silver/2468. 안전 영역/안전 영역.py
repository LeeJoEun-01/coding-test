import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
maxN = 0
inputs = []
for i in range(N):
    line = list(map(int, input().split()))
    inputs.append(line)
    tmp = max(line)
    if maxN < tmp:
        maxN = tmp
answer = [1]
not_visited = []
visited = []

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for n in range(1, maxN):
    ans = 0
    not_visited = []
    visited = [[0 for _ in range(N)]for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if inputs[i][j] <= n:
                visited[i][j] = 1
            else:
                not_visited.append([i, j])

    for i, j in not_visited:
        if visited[i][j] == 0:
            ans += 1
            deq = deque([[i, j]])

            while deq:
                x, y = deq.pop()

                for d in range(4):
                    newX = x + dx[d]
                    newY = y + dy[d]

                    if 0 <= newX < N and 0 <= newY < N:
                        if visited[newX][newY] == 0:
                            deq.appendleft([newX, newY])
                            visited[newX][newY] = 1
    # print(f"== n: {n} | ans: {ans}")
    answer.append(ans)

print(max(answer))