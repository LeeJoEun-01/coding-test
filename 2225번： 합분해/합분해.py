#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2225                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2225                           #+#        #+#      #+#     #
#    Solved: 2025/02/26 13:21:19 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
N, K = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(N+1)]for _ in range(K+1)]

for i in range(1,K+1):
  for j in range(N+1):
    if i == 1:
      dp[i][j] = 1
    else:
      if j == 0:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i][j-1]+dp[i-1][j]

print(dp[K][N]%1000000000)