import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

deq = deque([[0, 0]])
deq2 = deque([])
count = 0
ans = 0

while deq or deq2:
    cnt = 0
    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 0:
                    deq.append([nx, ny])
                    maps[nx][ny] = 3
                elif maps[nx][ny] == 1:
                    deq2.append([nx, ny])
                    maps[nx][ny] = 2
                    cnt += 1
    ans += 1

    deq = deq2
    deq2 = deque([])

    if cnt != 0:
        count = cnt

print(ans-1)
print(count)