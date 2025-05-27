#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11052                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11052                          #+#        #+#      #+#     #
#    Solved: 2025/05/17 15:44:15 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
dp = arr

for i in range(len(arr)):
    for j in range(0, i):
        dp[i] = max(dp[i-j-1]+dp[j], dp[i])

print(dp[N-1])
