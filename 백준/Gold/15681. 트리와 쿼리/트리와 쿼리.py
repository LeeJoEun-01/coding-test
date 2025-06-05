import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

c = [0]*(N+1)
visited = [False]*(N+1)


def dfs(r):
    visited[r] = True
    sub_count = 1

    for v in tree[r]:
        if not visited[v]:
            sub_count += dfs(v)

    c[r] = sub_count
    return sub_count


dfs(R)

for _ in range(Q):
    r = int(input().rstrip())
    print(c[r])