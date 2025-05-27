# DFS
# 1338. 바닥 장식

import sys

n, m = map(int, sys.stdin.readline().split())

floor = [list(map(str, sys.stdin.readline())) for _ in range(n)]
count = 0


# - 검사
for i in floor:
    target = ""
    for j in range(m):
        if target != i[j]:
            if i[j] != "|":
                count += 1
            target = i[j]

# | 검사
for i in range(m):
    target = ""
    for j in range(n):
        if target != floor[j][i]:
            if floor[j][i] != "-":
                count += 1
            target = floor[j][i]

print(count)
