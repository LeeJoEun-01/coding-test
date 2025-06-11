import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
tree = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(N-1):
    v1, v2 = map(int, input().split())

    tree[v1].append(v2)
    tree[v2].append(v1)

dp = [[0, 0] for _ in range(N+1)]


def check(v):
    visited[v] = True
    dp[v][0] = 0
    dp[v][1] = 1

    for i in (tree[v]):
        if not visited[i]:
            check(i)
            dp[v][0] += dp[i][1]
            dp[v][1] += min(dp[i][0], dp[i][1])


check(1)
print(min(dp[1][0], dp[1][1]))