#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2294                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2294                           #+#        #+#      #+#     #
#    Solved: 2025/01/30 23:38:14 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from math import inf
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(int(input().rstrip()))

dp = [inf]*(K+1)
dp[0] = 0

for target in arr:
  for i in range(target,K+1):
      dp[i] = min(dp[i], dp[i-target]+1)

if dp[K] == inf:
  print(-1)
else:
  print(dp[K])


# 1463. 1로 만들기

# import sys
# from math import inf
# input = sys.stdin.readline

# N = int(input().rstrip())
# dp = [0]*(N+1)

# for i in range(2, N+1):
#   dp[i] = dp[i-1]+1
#   if i%2 == 0:
#     dp[i] = min(dp[i], dp[i//2]+1)
#   if i%3 == 0:
#     dp[i] = min(dp[i], dp[i//3]+1)

# print(dp)
# print(dp[N])

# if N >=2 :
#   dp = [inf]*(N+1)
#   dp[0] = 0
#   dp[1] = 0

#   for i in range(2, N+1):
#     if i%2 == 0 and i%3 == 0:
#       dp[i] = min(dp[i//2], dp[i//3], dp[i-1])+1
#     elif i%2 == 0:
#       dp[i] = min(dp[i//2], dp[i-1])+1
#     elif i%3 == 0:
#       dp[i] = min(dp[i//3], dp[i-1])+1
#     else:
#       dp[i] = dp[i-1]+1
#   # print(dp)
#   print(dp[N])
# else:
#   print(0)