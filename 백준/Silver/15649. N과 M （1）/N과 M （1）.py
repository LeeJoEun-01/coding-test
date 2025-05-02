import sys

N, M = map(int, sys.stdin.readline().split())
ans = []


def backTraking():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            backTraking()
            ans.pop()


backTraking()
