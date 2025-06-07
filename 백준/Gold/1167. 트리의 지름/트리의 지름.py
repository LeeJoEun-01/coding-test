import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    inputs = list(map(int, input().split()))
    v1 = inputs[0]
    for i in range(1, len(inputs), 2):
        v2 = inputs[i]
        if v2 == -1:
            continue
        d = inputs[i+1]
        graph[v1].append([v2, d])
        graph[v2].append([v1, d])

max_d = 0
max_index = 0
visited = [False for _ in range(N+1)]


def dfs(v, dd):
    global max_d
    global max_index
    visited[v] = True

    for v1, d in graph[v]:
        if visited[v1] != True:
            if max_d < dd+d:
                max_d = dd+d
                max_index = v1

            dfs(v1, dd+d)


dfs(1, 0)
max_d = 0
visited = [False for _ in range(N+1)]
dfs(max_index, 0)
print(max_d)
