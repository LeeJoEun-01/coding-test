#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16953                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16953                          #+#        #+#      #+#     #
#    Solved: 2024/08/14 17:36:05 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline()
A, B = map(int, input.split())
count = 1

while B > A:
  if B%2 == 0:
    B = B//2
    count += 1
  else:
    if (B-1)%10 == 0:
      B = (B-1)//10
      count += 1
    else:
      break
  # print(B)

if B == A:
  print(count)
else:
  print(-1)