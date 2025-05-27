#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1149                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1149                           #+#        #+#      #+#     #
#    Solved: 2024/09/16 17:38:28 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# red green red

# 39 32 

import sys

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

sum = 0
result = arr

for i in range(1,N):
  result[i][0] = min(result[i-1][1], result[i-1][2]) + arr[i][0]
  result[i][1] = min(result[i-1][0], result[i-1][2]) + arr[i][1]
  result[i][2] = min(result[i-1][0], result[i-1][1]) + arr[i][2]

print(min(result[N-1]))