import sys
input = sys.stdin.readline

N = int(input().rstrip())
cnt = 0
visited = [-1]*N


def check(now_row):
    for row in range(now_row):
        if visited[row] == visited[now_row] or (now_row-row) == abs(visited[now_row]-visited[row]):
            return False
    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1

    else:
        for col in range(N):
            visited[row] = col
            if check(row):
                dfs(row+1)


dfs(0)
print(cnt)