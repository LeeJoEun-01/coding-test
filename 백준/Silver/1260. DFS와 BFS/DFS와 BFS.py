import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


graph = [[] for _ in range(n+1)]
visited_DFS = [False]*(n+1)
visited_BFS = [False]*(n+1)

# 그래프 그리기
for i in input_list:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in graph:
    i.sort()

# print(graph)


def dfs(v):
    visited_DFS[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited_DFS[i]:
            dfs(i)


def bfs(start):
    deq = deque([start])
    visited_BFS[start] = True

    while deq:
        v = deq.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited_BFS[i]:
                deq.append(i)
                visited_BFS[i] = True


dfs(v)
print()
bfs(v)
