#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2960                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2960                           #+#        #+#      #+#     #
#    Solved: 2025/05/24 00:17:42 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# import sys
# N, K = map(int, sys.stdin.readline().split())

# nums = [0]*(N+1)
# count = 0

# for i in range(2, N+1):
#     for j in range(i, N+1, i):
#         if nums[j] == 0:
#             count += 1
#             nums[j] = 1
#             if count == K:
#                 print(j)

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(N)]
arr.sort()

ans = 0
for i in range(N):
    tmp = arr[i]*(N-i)
    if tmp > ans:
        ans = tmp
print(ans)
