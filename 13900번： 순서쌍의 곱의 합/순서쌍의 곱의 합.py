#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13900                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13900                          #+#        #+#      #+#     #
#    Solved: 2025/01/09 20:29:53 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
result = 0

n_sum = sum(arr)

for i in arr:
  result += i*(n_sum-i)

print(result//2)
# int(result/2)