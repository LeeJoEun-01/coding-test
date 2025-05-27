#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2293                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2293                           #+#        #+#      #+#     #
#    Solved: 2024/09/26 01:54:51 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
arr.sort()

dp = [0]*(K+1)
dp[0] = 1

for n in arr:
    # dp[n] += 1
    for i in range(n, K+1):
        dp[i] += dp[i-n]
    # print(dp)

print(dp[K])
