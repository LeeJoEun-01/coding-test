import sys
from collections import deque
input = sys.stdin.readline


def NCA(a, b, tree):
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


visited = []
tree = []
deq = deque([])
depth = []


def dfs():
    while deq:
        root = deq.popleft()
        visited[root] = True

        for v in (tree[root]):
            if visited[v] == False:
                deq.append(v)
                depth[v] = depth[root]+1


T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    tree = [[] for _ in range(N+1)]
    visited = [False]*(N+1)
    parent = [0]*(N+1)
    parent[0] = -1
    depth = [0]*(N+1)
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        parent[b] = a

    root = parent.index(0)
    deq.append(root)
    dfs()

    a, b = map(int, input().split())
    print(NCA(a, b, tree))