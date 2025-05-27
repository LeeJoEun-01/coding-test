#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2018                           #+#        #+#      #+#     #
#    Solved: 2025/01/23 20:04:47 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N = int(sys.stdin.readline().rstrip())

left, right = 1, 2
value = 3
count = 1

if N >= 2:
  while left < right:

    if N == value:
      count += 1

    if N >= value:
      right += 1
      value += right
    else:
      value -= left
      left += 1

print(count)
