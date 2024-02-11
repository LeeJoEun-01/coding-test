# Depth-First Search
# 2606. 바이러스

import sys

n = int(sys.stdin.readline())
couple = int(sys.stdin.readline())
input_arr = [list(map(int, sys.stdin.readline().split()))
             for _ in range(couple)]

graph = [[] for _ in range(n+1)]

for arr in input_arr:
    graph[arr[0]].append(arr[1])
    graph[arr[1]].append(arr[0])

# print(graph)

visited = [False]*(n+1)


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(visited.count(True)-1)
