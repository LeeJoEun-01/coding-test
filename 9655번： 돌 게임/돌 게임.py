#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9655                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9655                           #+#        #+#      #+#     #
#    Solved: 2024/12/07 00:19:02 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N = int(sys.stdin.readline().rstrip())

dp = [0 for _ in range(N+1)]

dp[1] = 1

if N >= 2:
  dp[2] = 2
if N >= 3:
  dp[3] = 1

if N > 4: 
  for i in range(4,N+1):
    if i%3 == 0:
      dp[i] = dp[i-3] + 1
    elif i%3 == 1:
      dp[i] = dp[i-1] + 1
    elif i%3 == 2:
      dp[i] = dp[i-1] + 1

if dp[N]%2 == 0:
  print("CY")
else:
  print("SK")