#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2304                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2304                           #+#        #+#      #+#     #
#    Solved: 2025/04/04 00:52:35 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input().rstrip())
pillars = [0]*1001
for _ in range(N):
  L, H = list(map(int, input().split()))
  pillars[L] = H

max_num = max(pillars)
max_index = pillars.index(max_num)

ans = 0
current = 0
for i in range(max_index+1):
  current = max(current,pillars[i])
  ans += current

current = 0
for i in range(1000, max_index, -1):
  current = max(current, pillars[i])
  ans += current

print(ans)