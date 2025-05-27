#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2565                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2565                           #+#        #+#      #+#     #
#    Solved: 2024/09/26 00:34:03 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])

dp = [1]*N

for i in range(N):
    for j in range(i):

        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))
