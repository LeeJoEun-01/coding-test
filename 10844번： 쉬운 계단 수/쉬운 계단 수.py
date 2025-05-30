#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10844                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10844                          #+#        #+#      #+#     #
#    Solved: 2024/09/17 00:09:32 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N = int(sys.stdin.readline().rstrip())

dp = [[[0] for _ in range(10)] for _ in range(N) ]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1,N):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i-1][1]
    elif j == 9:
      dp[i][j] = dp[i-1][8]
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

result = sum(dp[N-1])
# print(dp)
print(result%1000000000)