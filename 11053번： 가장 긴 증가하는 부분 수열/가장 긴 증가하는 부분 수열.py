#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11053                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11053                          #+#        #+#      #+#     #
#    Solved: 2024/09/23 18:07:37 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

A = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

result = [1 for _ in range(A)]

for i in range(1,A):
  for j in range(0,i):
    if arr[j] < arr[i]:
      result[i] = max(result[i], result[j]+1)

print(max(result))

