#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2563                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2563                           #+#        #+#      #+#     #
#    Solved: 2025/05/23 00:30:13 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]
maps = [[0]*100 for i in range(100)]

for i in range(N):
    x, y = arr[i]

    for xx in range(x, x+10):
        for yy in range(y, y+10):
            maps[xx][yy] = 1

ans = 0
for i in range(100):
    count = maps[i].count(1)
    ans += count

print(ans)
