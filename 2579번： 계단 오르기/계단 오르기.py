#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2579                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2579                           #+#        #+#      #+#     #
#    Solved: 2024/12/09 00:51:33 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(n):
  arr.append(int(sys.stdin.readline().rstrip()))

dp = [0 for _ in range(n+1)]

dp[1] = arr[0]

if n >= 2:
  dp[2] = arr[0]+arr[1]
if n >= 3:
  dp[3] = max(arr[0],arr[1])+arr[2]
if n >= 4:
  dp[4] = arr[0] + max(arr[1],arr[2])+arr[3]

if n > 5:
  for i in range(5,n+1):
    dp[i] = max(dp[i-3]+arr[i-2]+arr[i-1], dp[i-2]+arr[i-1])

print(dp[n])