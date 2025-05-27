#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14728                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14728                          #+#        #+#      #+#     #
#    Solved: 2024/12/13 03:25:19 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N, T = map(int,sys.stdin.readline().split())

dp = [0]*(T+1)

for _ in range(N):
    K, S = map(int,sys.stdin.readline().split())
    for i in range(T, -1, -1):
        if i >= K:
            # print(f"=== i:{i} | K:{K} | S:{S}")
            # print(f"=== dp[i]: max({dp[i]}, {dp[i-K]+S})")
            dp[i] = max(dp[i], dp[i-K]+S)

print(dp[T])