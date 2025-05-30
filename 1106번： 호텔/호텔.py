#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1106                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1106                           #+#        #+#      #+#     #
#    Solved: 2024/12/17 17:10:34 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import math

C, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [math.inf for _ in range(C+100)]
dp[0] = 0

for i in range(N):
  cost = arr[i][0]
  num = arr[i][1]
  for j in range(num, C+100):
    dp[j] = min(dp[j-num]+cost, dp[j])

print(min(dp[C:]))