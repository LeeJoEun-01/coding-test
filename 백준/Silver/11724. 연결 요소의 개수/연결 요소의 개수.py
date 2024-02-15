import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
visited[0] = True

for gra in num_list:
    graph[gra[0]].append(gra[1])
    graph[gra[1]].append(gra[0])


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(1)
count = 1
while visited.count(False) != 0:
    v = visited.index(False)
    dfs(v)
    count += 1

print(count)
