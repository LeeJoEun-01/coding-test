
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
tree = [[] for _ in range(N+1)]
depth = [0]*(N+1)
parent = [0]*(N+1)
visited = [False]*(N+1)

for i in range(N-1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)


def bfs(s):
    deq = deque()
    deq.append(s)
    while deq:
        node = deq.popleft()
        visited[node] = True
        for i in tree[node]:
            if not visited[i]:
                depth[i] = depth[node]+1
                parent[i] = node
                deq.append(i)


def LCA(a, b):
    if depth[a] < depth[b]:
        tmp = a
        a = b
        b = tmp
    diff = depth[a] - depth[b]
    for _ in range(diff):
        a = parent[a]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


bfs(1)

T = int(input().rstrip())
for _ in range(T):
    a, b = map(int, input().split())
    print(LCA(a, b))
