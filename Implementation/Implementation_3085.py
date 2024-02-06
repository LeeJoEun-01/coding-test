# Implementation
# 3085. 사탕 게임

import sys

n = int(sys.stdin.readline())
arr_2d = [list(map(str, sys.stdin.readline())) for _ in range(n)]


def check():
    max_check_count = 0

    for i in range(n):
        count = 0
        for j in range(n-1):
            # 열검사 -
            if arr_2d[i][j] == arr_2d[i][j+1]:
                count += 1
            else:
                count = 0

            if max_check_count < count:
                max_check_count = count

    for i in range(n):
        count = 0
        for j in range(n-1):
            # 행검사 |
            if arr_2d[j][i] == arr_2d[j+1][i]:
                count += 1
            else:
                count = 0
            # print("| j: {} | i: {} | count: {}".format(j, i, count))

            if max_check_count < count:
                max_check_count = count

    return max_check_count


# 열검사 -
max_count = 0
check_count = 0

for i in range(n):
    for j in range(n):
        if j+1 < n and arr_2d[i][j] != arr_2d[i][j+1]:  # 오른쪽
            temp = arr_2d[i][j]
            arr_2d[i][j] = arr_2d[i][j+1]
            arr_2d[i][j+1] = temp
            check_count = check()
            arr_2d[i][j+1] = arr_2d[i][j]
            arr_2d[i][j] = temp

        if max_count < check_count:
            max_count = check_count

        if i+1 < n and arr_2d[i][j] != arr_2d[i+1][j]:  # 밑
            temp = arr_2d[i][j]
            arr_2d[i][j] = arr_2d[i+1][j]
            arr_2d[i+1][j] = temp
            check_count = check()
            arr_2d[i+1][j] = arr_2d[i][j]
            arr_2d[i][j] = temp

        if max_count < check_count:
            max_count = check_count

print(max_count+1)
