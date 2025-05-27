#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11659                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11659                          #+#        #+#      #+#     #
#    Solved: 2024/08/31 16:22:10 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 0 5 9 12 14 15
# 12 - 0
# 14 - 5 = 9


import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
index_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

sum_arr = [0]
val = 0
for i in arr:
  val += i
  sum_arr.append(val)

for i, j in index_arr:
  print(sum_arr[j]-sum_arr[i-1])