import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
visited = [False]*(N+1)
isDone = False

for _ in range(N-1):
    v1, v2, d = map(int, input().split())
    tree[v1].append([v2, d])
    tree[v2].append([v1, d])


def find_tree(v, d, end):
    global isDone
    dis = 0
    visited[v] = True

    if v == end:
        dis = d
        isDone = True
        return dis

    for i in tree[v]:
        if visited[i[0]] == False and isDone == False:
            dis = d
            dis += find_tree(i[0], i[1], end)
    return dis


for _ in range(M):
    v1, v2 = map(int, input().split())
    visited = [False]*(N+1)
    isDone = False

    dis = find_tree(v1, 0, v2)
    print(dis)