import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX_SIZE = 100001

deq = deque()
deq.append(N)

visited = [-1]*MAX_SIZE
visited[N] = 0

min_cnt = 0

while deq:
    v = deq.popleft()

    if v == K:
        min_cnt += 1

    for next in [v+1, v-1, v*2]:
        if 0 <= next < MAX_SIZE:
            if visited[next] == -1 or visited[next] >= visited[v]+1:
                visited[next] = visited[v]+1
                deq.append(next)

print(visited[K])
print(min_cnt)