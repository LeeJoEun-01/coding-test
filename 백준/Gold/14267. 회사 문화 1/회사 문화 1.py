import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
parents = list(map(int, input().split()))
tree = [[] for _ in range(n+1)]

for i in range(n):
    p = parents[i]
    if p != -1:
        tree[p].append(i+1)

result = [0]*n
deq = deque()


def dfs():

    while deq:
        v = deq.popleft()

        for i in tree[v]:
            result[i-1] += result[v-1]
            deq.append(i)


for i in range(m):
    num, w = map(int, input().split())
    result[num-1] += w

deq.append(1)
dfs()
print(*result)